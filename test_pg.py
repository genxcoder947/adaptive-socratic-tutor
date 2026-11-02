import psycopg2
from getpass import getpass

try:
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="mentor_db",
        user="postgres",
        password=getpass("Enter PostgreSQL password: ")
    )

    print("PostgreSQL connection successful!")

    cursor = conn.cursor()
    cursor.execute("SELECT current_database();")
    print("Connected database:", cursor.fetchone()[0])

    cursor.close()
    conn.close()

except Exception as e:
    print("Connection failed:", e)
    