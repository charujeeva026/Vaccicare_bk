import psycopg2
import os

# Possible local connection strings
LOCAL_URLS = [
    "postgresql://postgres:sarukumar%402008@localhost:5432/postgres",
    "postgresql://postgres@localhost:5432/postgres", # Try without password
    "postgresql://postgres:admin@localhost:5432/postgres",
    "postgresql://postgres:root@localhost:5432/postgres",
]

def check_local():
    for url in LOCAL_URLS:
        try:
            print(f"Trying connection: {url}")
            conn = psycopg2.connect(url, connect_timeout=3)
            cur = conn.cursor()
            print("Connected successfully!")
            
            cur.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                AND table_type = 'BASE TABLE'
            """)
            tables = [row[0] for row in cur.fetchall()]
            
            if 'hospital' in tables:
                cur.execute("SELECT COUNT(*) FROM hospital")
                count = cur.fetchone()[0]
                print(f"Found table 'hospital' with {count} rows.")
                if count > 0:
                    print("THIS IS THE SOURCE!")
                    # List first few hospitals
                    cur.execute("SELECT hospital_name FROM hospital LIMIT 5")
                    print(f"Sample data: {cur.fetchall()}")
                    return url
            else:
                print(f"Table 'hospital' not found in public schema. Found: {tables}")
            
            conn.close()
        except Exception as e:
            print(f"Failed to connect: {e}")
    return None

if __name__ == "__main__":
    check_local()
