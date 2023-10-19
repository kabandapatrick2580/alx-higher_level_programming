-- a script that creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use database
USE hbtn_0d_usa;
-- script to create table
CREATE TABLE IF NOT EXISTS cities (
        id INT UNIQUE AUTO_INCREMENT NOT NULL,
        state_id INT NOT NULL,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY (state_id) REFERENCES states(id)
)
