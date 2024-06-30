-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;

-- Switch to the database
USE hbtn_0e_0_usa;

-- Create the states table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert initial data into the states table
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
