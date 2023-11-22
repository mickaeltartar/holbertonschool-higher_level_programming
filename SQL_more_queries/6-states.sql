-- create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- switch to this table

USE hbtn_0d_usa;

-- create a table

CREATE TABLE IF NOT EXISTS states(
id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
name VARCHAR(256)NOT NULL
);
