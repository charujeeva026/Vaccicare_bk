import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# SOURCE DATABASE (Local)
OLD_DB_URL = "postgresql://postgres:AcademyRootPassword@localhost:5432/vaccicare_new"

# TARGET DATABASE (Neon)
NEW_DB_URL = os.getenv("database_url")

# ORDERED TABLES TO PREVENT FK VIOLATIONS
TABLE_ORDER = [
    'hospital',
    'client',
    'doctor',
    'baby',
    'vaccine',
    'vaccine_records',
    'health_record',
    'appointment',
    'reminders'
]

def migrate():
    try:
        print(f"Connecting to source and target...")
        old_conn = psycopg2.connect(OLD_DB_URL)
        old_cur = old_conn.cursor()
        new_conn = psycopg2.connect(NEW_DB_URL)
        new_cur = new_conn.cursor()

        for table in TABLE_ORDER:
            print(f"Migrating table: {table}")
            old_cur.execute(f"SELECT * FROM {table}")
            rows = old_cur.fetchall()
            
            if not rows:
                print(f" - {table} is empty.")
                continue

            old_cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}' ORDER BY ordinal_position")
            columns = [row[0] for row in old_cur.fetchall()]
            col_string = ",".join(columns)
            placeholders = ",".join(["%s"] * len(columns))
            
            # Use ON CONFLICT DO NOTHING to avoid duplicates if re-running
            insert_query = f"INSERT INTO {table} ({col_string}) VALUES ({placeholders}) ON CONFLICT DO NOTHING"
            
            try:
                new_cur.executemany(insert_query, rows)
                new_conn.commit()
                print(f" - Success: {len(rows)} rows processed.")
            except Exception as e:
                new_conn.rollback()
                print(f" - Error in {table}: {e}")

        print("Final migration completed successfully!")

    except Exception as e:
        print(f"Fatal error: {e}")
    finally:
        if 'old_conn' in locals(): old_conn.close()
        if 'new_conn' in locals(): new_conn.close()

if __name__ == "__main__":
    migrate()
