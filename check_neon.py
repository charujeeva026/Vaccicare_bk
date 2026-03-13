import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# Neon URL should be in .env now
NEW_DB_URL = os.getenv("database_url")

def check_neon():
    try:
        print(f"Connecting to Neon (Target)...")
        conn = psycopg2.connect(NEW_DB_URL)
        cur = conn.cursor()

        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            AND table_type = 'BASE TABLE'
        """)
        tables = [row[0] for row in cur.fetchall()]
        
        print(f"Checking row counts for {len(tables)} tables:")
        for table in tables:
            cur.execute(f"SELECT COUNT(*) FROM {table}")
            count = cur.fetchone()[0]
            print(f"Table: {table} -> Count: {count}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    check_neon()
