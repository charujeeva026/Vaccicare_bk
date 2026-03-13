import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# OLD DATABASE (Supabase)
OLD_DB_URL = os.getenv("database_url")

# NEW DATABASE (Neon)
NEW_DB_URL = "postgresql://neondb_owner:npg_fsXt9iMocEw0@ep-still-art-a4t1vjp7-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

def migrate():
    if not OLD_DB_URL or not NEW_DB_URL or "PASTE" in NEW_DB_URL:
        print("Error: Please provide both OLD_DB_URL and NEW_DB_URL in the script or .env")
        return

    try:
        # Connect to old database
        print(f"Connecting to old database...")
        old_conn = psycopg2.connect(OLD_DB_URL)
        old_cur = old_conn.cursor()

        # Connect to new database
        print(f"Connecting to new database...")
        new_conn = psycopg2.connect(NEW_DB_URL)
        new_cur = new_conn.cursor()

        # 1. Get all tables
        old_cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            AND table_type = 'BASE TABLE'
        """)
        tables = [row[0] for row in old_cur.fetchall()]
        print(f"Found tables: {tables}")

        for table in tables:
            print(f"Migrating table: {table}")
            
            # Get data from old table
            old_cur.execute(f"SELECT * FROM {table}")
            rows = old_cur.fetchall()
            
            if not rows:
                print(f"Table {table} is empty. Skipping.")
                continue

            # Get column names
            old_cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}' ORDER BY ordinal_position")
            columns = [row[0] for row in old_cur.fetchall()]
            col_string = ",".join(columns)
            placeholders = ",".join(["%s"] * len(columns))
            
            # Disable triggers/constraints for cleaner import if needed, but for simple schemas this might work
            insert_query = f"INSERT INTO {table} ({col_string}) VALUES ({placeholders}) ON CONFLICT DO NOTHING"
            
            try:
                new_cur.executemany(insert_query, rows)
                new_conn.commit()
                print(f"Successfully migrated {len(rows)} rows to {table}")
            except Exception as e:
                new_conn.rollback()
                print(f"Failed to migrate table {table}: {e}")

        print("Migration process finished.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'old_conn' in locals(): old_conn.close()
        if 'new_conn' in locals(): new_conn.close()

if __name__ == "__main__":
    migrate()
