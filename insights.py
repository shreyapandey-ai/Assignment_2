# insights.py
import sqlite3

def users_per_city():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT city, COUNT(*) 
        FROM users 
        GROUP BY city
    """)

    for row in cur.fetchall():
        print(row)

    conn.close()
