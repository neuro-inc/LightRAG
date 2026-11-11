import asyncio
from contextlib import asynccontextmanager
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from lightrag.kg.postgres_impl import PostgreSQLDB

pytestmark = pytest.mark.offline


def make_db(attempts: int = 3) -> PostgreSQLDB:
    return PostgreSQLDB(
        {
            "host": "localhost",
            "port": 5432,
            "user": "postgres",
            "password": "postgres",
            "database": "postgres",
            "workspace": "test_ws",
            "max_connections": 10,
            "connection_retry_attempts": attempts,
            "connection_retry_backoff": 0,
            "connection_retry_backoff_max": 0,
            "pool_close_timeout": 5.0,
            "enable_vector": False,
        }
    )


def make_pool(connection: MagicMock) -> MagicMock:
    @asynccontextmanager
    async def acquire(timeout=None):
        yield connection

    pool = MagicMock()
    pool.acquire = acquire
    pool.close = AsyncMock()
    return pool


def refused() -> ConnectionRefusedError:
    return ConnectionRefusedError(111, "refused")


@pytest.mark.asyncio
async def test_initdb_retry_does_not_wait_on_the_reconnect_lock():
    db = make_db()
    pool = MagicMock()
    create_pool = AsyncMock(side_effect=[refused(), pool])

    with patch("lightrag.kg.postgres_impl.asyncpg.create_pool", create_pool):
        async with db._pool_reconnect_lock:
            await asyncio.wait_for(db.initdb(), timeout=5)

    assert db.pool is pool
    assert create_pool.await_count == 2


@pytest.mark.asyncio
async def test_ensure_pool_makes_one_attempt_and_releases_the_lock():
    db = make_db()
    create_pool = AsyncMock(side_effect=refused())

    with patch("lightrag.kg.postgres_impl.asyncpg.create_pool", create_pool):
        with pytest.raises(ConnectionRefusedError):
            await asyncio.wait_for(db._ensure_pool(), timeout=5)

    assert db.pool is None
    assert create_pool.await_count == 1
    assert not db._pool_reconnect_lock.locked()


@pytest.mark.asyncio
async def test_query_recovers_after_the_database_comes_back():
    db = make_db()
    connection = MagicMock()
    connection.fetch = AsyncMock(return_value=[])
    create_pool = AsyncMock(side_effect=[refused(), refused(), make_pool(connection)])

    with patch("lightrag.kg.postgres_impl.asyncpg.create_pool", create_pool):
        await asyncio.wait_for(db.query("SELECT 1"), timeout=5)

    connection.fetch.assert_awaited_once_with("SELECT 1")
    assert create_pool.await_count == 3
    assert not db._pool_reconnect_lock.locked()


@pytest.mark.asyncio
async def test_query_fails_after_the_configured_attempts():
    db = make_db(attempts=2)
    create_pool = AsyncMock(side_effect=refused())

    with patch("lightrag.kg.postgres_impl.asyncpg.create_pool", create_pool):
        with pytest.raises(ConnectionRefusedError):
            await asyncio.wait_for(db.query("SELECT 1"), timeout=5)

    assert create_pool.await_count == 2
    assert not db._pool_reconnect_lock.locked()


@pytest.mark.asyncio
async def test_check_connection_selects_one():
    db = make_db()
    connection = MagicMock()
    connection.fetchval = AsyncMock(return_value=1)

    with patch(
        "lightrag.kg.postgres_impl.asyncpg.create_pool",
        AsyncMock(return_value=make_pool(connection)),
    ):
        await db.check_connection(timeout=5)

    connection.fetchval.assert_awaited_once_with("SELECT 1")


@pytest.mark.asyncio
async def test_check_connection_raises_when_the_database_is_down():
    db = make_db()

    with patch(
        "lightrag.kg.postgres_impl.asyncpg.create_pool",
        AsyncMock(side_effect=refused()),
    ):
        with pytest.raises(ConnectionRefusedError):
            await db.check_connection(timeout=5)

    assert not db._pool_reconnect_lock.locked()


@pytest.mark.asyncio
async def test_check_connection_times_out_on_a_hanging_database():
    db = make_db()
    connection = MagicMock()

    async def hang(_sql):
        await asyncio.sleep(60)

    connection.fetchval = AsyncMock(side_effect=hang)

    with patch(
        "lightrag.kg.postgres_impl.asyncpg.create_pool",
        AsyncMock(return_value=make_pool(connection)),
    ):
        with pytest.raises(asyncio.TimeoutError):
            await db.check_connection(timeout=0.1)
