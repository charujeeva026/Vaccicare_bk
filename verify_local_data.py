import psycopg2
import os

LOCAL_URL = "postgresql://postgres:AcademyRootPassword@localhost:5432/vaccicare_new"

def verify_source():
    try:
        print(f"Connecting to local database: vaccicare_new")
        conn = psycopg2.connect(LOCAL_URL)
        cur = conn.cursor()
        
        cur.execute("SELECT COUNT(*) FROM hospital")
        count = cur.fetchone()[0]
        print(f"Found {count} rows in 'hospital' table.")
        
        if count > 0:
            cur.execute("SELECT hospital_name, address FROM hospital LIMIT 3")
            print("Sample data:")
            for row in cur.fetchall():
                print(f" - {row[0]} at {row[1]}")
        
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    verify_source()
