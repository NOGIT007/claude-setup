# Database Commands

## Description
Database management commands for various database systems.

## Firestore (Google Cloud)
```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login to Firebase
firebase login

# Initialize Firestore
firebase init firestore

# Deploy security rules
firebase deploy --only firestore:rules

# Backup data
gcloud firestore export gs://my-bucket/backup-$(date +%Y%m%d)
```

## Neo4j Cypher Queries
```cypher
-- Show database schema
CALL db.schema.visualization()

-- List all node labels
CALL db.labels()

-- List all relationship types
CALL db.relationshipTypes()

-- Simple node query
MATCH (n:Person) RETURN n LIMIT 10

-- Create node with properties
CREATE (p:Person {name: 'John', age: 30})

-- Create relationship
MATCH (a:Person), (b:Person)
WHERE a.name = 'John' AND b.name = 'Jane'
CREATE (a)-[r:KNOWS]->(b)
```

## PostgreSQL
```bash
# Connect to database
psql -h localhost -U username -d database_name

# List databases
\l

# List tables
\dt

# Describe table
\d table_name

# Run SQL file
\i script.sql

# Backup database
pg_dump -h localhost -U username database_name > backup.sql
```

## Token Usage
Estimated: ~0.2k tokens

## Usage
Add this line to your CLAUDE.md for database support:
```
## Active Commands
- database: Database management commands and queries
```