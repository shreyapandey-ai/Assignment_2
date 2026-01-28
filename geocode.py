# geocode.py
import requests
import time
import sqlite3
import logging
from requests.exceptions import ReadTimeout, ConnectionError

DB_PATH = "geo_cache.db"
USER_AGENT = "geo_etl_app (shreya.pandey@highspring.in)"  # must exist

# --------------------------------------------------
# Init cache
# --------------------------------------------------
def init_cache():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS geocode_cache (
            city TEXT,
            zipcode TEXT,
            latitude REAL,
            longitude REAL,
            PRIMARY KEY (city, zipcode)
        )
    """)
    conn.commit()
    conn.close()

# --------------------------------------------------
# Cache lookup
# --------------------------------------------------
def get_from_cache(city, zipcode):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT latitude, longitude
        FROM geocode_cache
        WHERE city = ? AND zipcode = ?
    """, (city, zipcode))
    row = cur.fetchone()
    conn.close()
    return row

# --------------------------------------------------
# Save to cache
# --------------------------------------------------
def save_to_cache(city, zipcode, lat, lon):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT OR REPLACE INTO geocode_cache
        VALUES (?, ?, ?, ?)
    """, (city, zipcode, lat, lon))
    conn.commit()
    conn.close()

# --------------------------------------------------
# 🔧 THIS IS WHERE YOUR CODE GOES
# --------------------------------------------------
def fetch_from_api(city, zipcode, retries=3):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "city": city,
        "postalcode": zipcode,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": USER_AGENT
    }

    for attempt in range(retries):
        try:
            response = requests.get(
                url,
                params=params,
                headers=headers,
                timeout=30
            )

            if response.status_code != 200:
                return None, None

            data = response.json()
            if not data:
                return None, None

            return float(data[0]["lat"]), float(data[0]["lon"])

        except (ReadTimeout, ConnectionError):
            logging.warning(
                f"Geocode timeout ({attempt+1}/{retries}) for {city}, {zipcode}"
            )
            time.sleep(2)

    return None, None

# --------------------------------------------------
# Main entry
# --------------------------------------------------
def geocode(city, zipcode):
    if not city or not zipcode:
        return None, None

    cached = get_from_cache(city, zipcode)
    if cached:
        return cached

    lat, lon = fetch_from_api(city, zipcode)
    save_to_cache(city, zipcode, lat, lon)
    time.sleep(1)
    return lat, lon


init_cache()
