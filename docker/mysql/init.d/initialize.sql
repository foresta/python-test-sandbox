use sandbox;

CREATE TABLE IF NOT EXISTS users
(
  id           INT(10),
  name     VARCHAR(40)
);

TRUNCATE TABLE users;

INSERT INTO users (id, name) VALUES (1, 'Alice');
INSERT INTO users (id, name) VALUES (2, 'Bob');
INSERT INTO users (id, name) VALUES (3, 'Charlie');
INSERT INTO users (id, name) VALUES (4, 'David');
INSERT INTO users (id, name) VALUES (5, 'Eve');
INSERT INTO users (id, name) VALUES (6, 'Frank');
