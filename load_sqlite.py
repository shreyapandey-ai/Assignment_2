# load_sqlite.py
import sqlite3
import logging

def load_to_sqlite(users):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            city TEXT,
            zipcode TEXT
        )
    """)

    for u in users:
        cur.execute("""
            INSERT OR IGNORE INTO users VALUES (?, ?, ?, ?, ?)
        """, (
            u["user_id"], u["name"], u["email"], u["city"], u["zipcode"]
        ))

    conn.commit()
    conn.close()
    logging.info("Data inserted into SQLite")
