import os
import time
import psycopg
from psycopg.rows import dict_row
from typing import List, Dict, Optional
from dotenv import load_dotenv

# Load environment variables from .env.local or .env
load_dotenv(".env.local")
load_dotenv()

# Database Configuration
DB_CONFIG = {
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "postgres"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "dbname": os.getenv("DB_NAME", "lead_scraper")
}

def get_connection():
    """Create and return a connection to the PostgreSQL database."""
    conn_str = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
    return psycopg.connect(conn_str, row_factory=dict_row)

def init_db():
    """Initialize the PostgreSQL database and the leads table."""
    max_retries = 10
    retry_delay = 3
    
    # 1. Connect to default 'postgres' db to create our target db if it doesn't exist
    for attempt in range(max_retries):
        try:
            sys_conn_str = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/postgres"
            with psycopg.connect(sys_conn_str, autocommit=True) as conn:
                res = conn.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_CONFIG['dbname'],)).fetchone()
                if not res:
                    print(f"🛠️  Database '{DB_CONFIG['dbname']}' not found. Creating...")
                    conn.execute(f"CREATE DATABASE {DB_CONFIG['dbname']}")
                    print(f"✅ Database '{DB_CONFIG['dbname']}' created.")
                else:
                    print(f"✅ Database '{DB_CONFIG['dbname']}' exists.")
            break
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"⚠️  Database not ready (attempt {attempt + 1}/{max_retries}). Retrying in {retry_delay}s... Error: {e}")
                time.sleep(retry_delay)
            else:
                print(f"❌ Database Init Error: {e}")
                # We raise here because if DB doesn't exist/connect, app shouldn't start
                raise e

    # 2. Connect to the specific database to create the table
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute('''
                    CREATE TABLE IF NOT EXISTS leads (
                        id SERIAL PRIMARY KEY,
                        business_name VARCHAR(255),
                        industry VARCHAR(255),
                        category VARCHAR(255),
                        location VARCHAR(255),
                        address TEXT,
                        rating DECIMAL(3, 1),
                        review_count INT,
                        is_claimed BOOLEAN,
                        has_website BOOLEAN,
                        website_url TEXT,
                        phone VARCHAR(255),
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        UNIQUE (business_name, address)
                    )
                ''')
                conn.commit()
        print("✅ PostgreSQL Table 'leads' initialized.")
        
        # Initialize API key tables
        from app.db.api_keys import create_tables as create_api_key_tables
        create_api_key_tables()
    except Exception as e:
        print(f"❌ Table Init Error: {e}")

def insert_lead(lead: Dict):
    """Insert a lead into PostgreSQL. Returns True if added, False if duplicate."""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                query = '''
                    INSERT INTO leads (
                        business_name, industry, category, location, address, 
                        rating, review_count, is_claimed, 
                        has_website, website_url, phone
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (business_name, address) DO NOTHING
                    RETURNING id
                '''
                values = (
                    lead["business_name"],
                    lead["industry"],
                    lead.get("category"),
                    lead["location"],
                    lead["address"],
                    lead.get("rating"),
                    lead.get("review_count"),
                    lead.get("is_claimed"),
                    lead["has_website"],
                    lead["website_url"],
                    lead["phone"]
                )
                cur.execute(query, values)
                result = cur.fetchone()
                conn.commit()
                
                if result:
                    return True
                else:
                    return False
    except Exception as e:
        print(f"❌ Insert Error: {e}")
        return False

def get_all_leads():
    """Retrieve all leads from PostgreSQL for CSV export."""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM leads ORDER BY created_at DESC")
                rows = cur.fetchall()
                return rows
    except Exception as e:
        print(f"❌ Fetch Error: {e}")
        return []
