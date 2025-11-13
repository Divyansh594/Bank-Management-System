-- Schema for Bank Management System
-- Matches tables used by the Python program

CREATE DATABASE IF NOT EXISTS bank;
USE bank;

-- Drop and recreate tables to ensure a clean setup
DROP TABLE IF EXISTS amount;
DROP TABLE IF EXISTS account;

CREATE TABLE account (
  accno INT PRIMARY KEY,
  name VARCHAR(100),
  dob VARCHAR(50),
  address VARCHAR(255),
  phone INT,
  opening_balance INT
);

CREATE TABLE amount (
  accno INT PRIMARY KEY,
  name VARCHAR(100),
  balance INT
);