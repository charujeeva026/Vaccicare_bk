import psycopg2
import os
from dotenv import load_dotenv

# We need the OLD URL which was in .env before I changed it.
# I will use the one I saw in the previous view_file of .env:
# postgresql://postgres.bixthsmizplgqdcmtrjd:sarukumar%402008@aws-1-ap-south-1.pooler.supabase.com:5432/postgres

OLD_DB_URL = "postgresql://postgres.bixthsmizplgqdcmtrjd:sarukumar%402008@aws-1-ap-south-1.pooler.supabase.com:5432/postgres"

def check_data():
    try:
        print(f"Connecting to Supabase (Source)...")
        conn = psycopg2.connect(OLD_DB_URL)
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
    check_data()
