
--In this assignment, you will use the SQLite browser to make a database, insert some data and then run  query.
create database example;
use example;

CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
);
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Derryne', 21);
INSERT INTO Ages (name, age) VALUES ('Olaoluwapolorimi', 36);
INSERT INTO Ages (name, age) VALUES ('Jole', 19);
INSERT INTO Ages (name, age) VALUES ('Aara', 26);

SELECT hex(name || age) AS X FROM Ages ORDER BY X;


