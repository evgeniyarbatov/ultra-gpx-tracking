CREATE TABLE distances (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    userid VARCHAR(255) NOT NULL,
    distance FLOAT NOT NULL
);