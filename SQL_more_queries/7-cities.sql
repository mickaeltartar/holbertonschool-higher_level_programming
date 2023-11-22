-- create a database

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- switch to this database

USE hbtn_0d_usa;

-- create table & set it

CREATE TABLE IF NOT EXISTS cities(
id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
