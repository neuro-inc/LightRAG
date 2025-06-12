-- PostgreSQL initialization script for Cost-Effective stack
-- Enable required extensions for LightRAG

-- Enable pgvector extension for vector operations
CREATE EXTENSION IF NOT EXISTS vector;

-- Enable additional useful extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Grant necessary permissions
GRANT ALL PRIVILEGES ON DATABASE lightrag TO lightrag_user;

-- Create schemas if needed
CREATE SCHEMA IF NOT EXISTS lightrag_vectors;
CREATE SCHEMA IF NOT EXISTS lightrag_kv;
CREATE SCHEMA IF NOT EXISTS lightrag_docs;

-- Grant schema permissions
GRANT ALL ON SCHEMA lightrag_vectors TO lightrag_user;
GRANT ALL ON SCHEMA lightrag_kv TO lightrag_user;
GRANT ALL ON SCHEMA lightrag_docs TO lightrag_user;