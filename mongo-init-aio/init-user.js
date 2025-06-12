// MongoDB initialization script for All-in-One stack
// Create LightRAG user and database

db = db.getSiblingDB('admin');

// Create LightRAG user
db.createUser({
  user: 'lightrag_user',
  pwd: 'lightrag_pass',
  roles: [
    {
      role: 'readWrite',
      db: 'lightrag'
    }
  ]
});

// Switch to LightRAG database
db = db.getSiblingDB('lightrag');

// Create initial collection
db.createCollection('doc_status');

print('LightRAG MongoDB user and database initialized successfully');