import mysql.connector
import os
from typing import List, Dict, Optional
from mysql.connector import Error

# Database Configuration for XAMPP
# You can change these values here or move them to an .env file later
DB_CONFIG = {
    "user": "root",        # Default XAMPP user
    "password": "",        # Default XAMPP password is empty
    "host": "localhost",
    "port": 3306,
    "database": "leadly"
}

def get_connection():
    """Create and return a connection to the MySQL database."""
    return mysql.connector.connect(**DB_CONFIG)

def init_db():
    """Initialize the MySQL database and the leads table."""
    try:
        # 1. Connect without a database to create it if it doesn't exist
        conn = mysql.connector.connect(
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"]
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        conn.commit()
        cursor.close()
        conn.close()

        # 2. Connect to the specific database to create the table
        conn = get_connection()
        cursor = conn.cursor()
        
        # MySQL requires lengths for TEXT/VARCHAR columns in UNIQUE constraints
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INT AUTO_INCREMENT PRIMARY KEY,
                business_name VARCHAR(255),
                industry VARCHAR(255),
                location VARCHAR(255),
                address VARCHAR(500),
                has_website BOOLEAN,
                website_url TEXT,
                phone VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE KEY unique_lead (business_name, address(255))
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ MySQL Database & Table initialized.")
    except Error as e:
        print(f"❌ MySQL Init Error: {e}")

def insert_lead(lead: Dict):
    """Insert a lead into MySQL. Returns True if added, False if duplicate."""
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = '''
            INSERT INTO leads (business_name, industry, location, address, has_website, website_url, phone)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        values = (
            lead["business_name"],
            lead["industry"],
            lead["location"],
            lead["address"],
            lead["has_website"],
            lead["website_url"],
            lead["phone"]
        )
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        return True
    except mysql.connector.IntegrityError:
        # Duplicate based on UNIQUE KEY
        return False
    except Error as e:
        print(f"❌ MySQL Insert Error: {e}")
        return False
    finally:
        if conn and conn.is_connected():
            conn.close()

def get_all_leads():
    """Retrieve all leads from MySQL for CSV export."""
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM leads ORDER BY created_at DESC")
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except Error as e:
        print(f"❌ MySQL Fetch Error: {e}")
        return []
    finally:
        if conn and conn.is_connected():
            conn.close()