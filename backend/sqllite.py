"""SQLLITE INITALIZES and creates tables """

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

#Create user table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
)''')

# Create Customer table
cursor.execute('''CREATE TABLE IF NOT EXISTS Customer (
    first_name VARCHAR(200),
    last_name VARCHAR(200),
    phone_no INTEGER,
    email_address VARCHAR(50),
    address VARCHAR(500),
    postal_code VARCHAR(10),
    animal_type VARCHAR(200)
)''')

# Create Pet_Type table
cursor.execute('''CREATE TABLE IF NOT EXISTS Pet_Type (
    specific_breed VARCHAR(200),
    service_type VARCHAR(200),
    hyper_allergenic VARCHAR(200),
    house_trained VARCHAR(200)
)''')

# Create specific_breed table
cursor.execute('''CREATE TABLE IF NOT EXISTS specific_breed (
    Breed VARCHAR(200) PRIMARY KEY,
    Life_Span VARCHAR(200),
    Characteristics VARCHAR(200)
)''')

# Create service_type table
cursor.execute('''CREATE TABLE IF NOT EXISTS service_type (
    service_type VARCHAR(200) REFERENCES Pet_Type(service_type),
    Name VARCHAR(200),
    Breed VARCHAR(200),
    Service INTEGER,
    Age VARCHAR(200),
    Status VARCHAR(200),
    Updated VARCHAR(200)
)''')

# Create hyper_allergenic table
cursor.execute('''CREATE TABLE IF NOT EXISTS hyper_allergenic (
    hyper_allergenic VARCHAR(200) REFERENCES Pet_Type(hyper_allergenic),
    Name VARCHAR(200),
    Breed VARCHAR(200),
    Training VARCHAR(200),
    Age INTEGER,
    Status VARCHAR(200),
    Updated VARCHAR(200)
)''')

# Create house_trained table
cursor.execute('''CREATE TABLE IF NOT EXISTS house_trained (
    house_trained VARCHAR(200) REFERENCES Pet_Type(house_trained),
    Name VARCHAR(200),
    Breed VARCHAR(200),
    Age INTEGER,
    Status VARCHAR(200),
    Updated VARCHAR(200)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dark_mode TEXT NOT NULL,
    text_size INTEGER NOT NULL,
    image_size INTEGER NOT NULL,
    high_contrast TEXT NOT NULL
)''')

cursor.execute('''DROP TABLE IF EXISTS PETS''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    breed TEXT NOT NULL,
    specific_breed TEXT NOT NULL,
    service_type TEXT NOT NULL,
    hyper_allergenic TEXT NOT NULL,
    house_trained TEXT NOT NULL,
    img_src VARCHAR(200),
    animal_type TEXT NOT NULL CHECK (animal_type IN ("dog", "cat"))
)''')

#Creating tables for shop
cursor.execute('''CREATE TABLE IF NOT EXISTS Items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
    description TEXT,
    cost REAL,
    stock INTEGER,
    category TEXT NOT NULL
)''')

# Commit changes and close the connection
conn.commit()
conn.close()
