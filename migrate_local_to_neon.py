import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# SOURCE DATABASE (Local)
OLD_DB_URL = "postgresql://postgres:AcademyRootPassword@localhost:5432/vaccicare_new"

# TARGET DATABASE (Neon)
NEW_DB_URL = os.getenv("database_url")

def migrate():
    if not OLD_DB_URL or not NEW_DB_URL:
        print("Error: URLs missing.")
        return

    try:
        print(f"Connecting to source: local vaccicare_new")
        old_conn = psycopg2.connect(OLD_DB_URL)
        old_cur = old_conn.cursor()

        print(f"Connecting to target: Neon")
        new_conn = psycopg2.connect(NEW_DB_URL)
        new_cur = new_conn.cursor()

        old_cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            AND table_type = 'BASE TABLE'
        """)
        tables = [row[0] for row in old_cur.fetchall()]
        print(f"Tables to migrate: {tables}")

        for table in tables:
            print(f"Processing table: {table}")
            old_cur.execute(f"SELECT * FROM {table}")
            rows = old_cur.fetchall()
            
            if not rows:
                print(f" - {table} is empty. Skipping.")
                continue

            old_cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}' ORDER BY ordinal_position")
            columns = [row[0] for row in old_cur.fetchall()]
            col_string = ",".join(columns)
            placeholders = ",".join(["%s"] * len(columns))
            
            insert_query = f"INSERT INTO {table} ({col_string}) VALUES ({placeholders}) ON CONFLICT DO NOTHING"
            
            try:
                new_cur.executemany(insert_query, rows)
                new_conn.commit()
                print(f" - Migrated {len(rows)} rows to {table}")
            except Exception as e:
                new_conn.rollback()
                print(f" - Error migrating {table}: {e}")

        print("Migration finished!")

    except Exception as e:
        print(f"Fatal error: {e}")
    finally:
        if 'old_conn' in locals(): old_conn.close()
        if 'new_conn' in locals(): new_conn.close()

if __name__ == "__main__":
    migrate()
