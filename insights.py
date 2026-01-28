# insights.py
import sqlite3

DB = "users.db"

def users_per_city():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        SELECT city, COUNT(*) 
        FROM users 
        GROUP BY city
        ORDER BY COUNT(*) DESC
    """)

    for row in cur.fetchall():
        print(row)

    conn.close()


def users_by_geo_bucket():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            ROUND(latitude, 1) AS lat_bucket,
            ROUND(longitude, 1) AS lon_bucket,
            COUNT(*) AS users
        FROM users
        WHERE latitude IS NOT NULL AND longitude IS NOT NULL
        GROUP BY lat_bucket, lon_bucket
        ORDER BY users DESC
    """)

    for row in cur.fetchall():
        print(row)

    conn.close()


def user_density():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        SELECT city,
               COUNT(*) AS users,
               COUNT(DISTINCT zipcode) AS zipcodes,
               ROUND(1.0 * COUNT(*) / COUNT(DISTINCT zipcode), 2) AS density
        FROM users
        WHERE city IS NOT NULL
        GROUP BY city
        HAVING zipcodes > 0
        ORDER BY density DESC
    """)

    for row in cur.fetchall():
        print(row)

    conn.close()


def geo_coverage():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            COUNT(*) AS total,
            SUM(latitude IS NOT NULL AND longitude IS NOT NULL) AS geocoded,
            SUM(latitude IS NULL OR longitude IS NULL) AS missing
        FROM users
    """)

    print(cur.fetchone())
    conn.close()


def hemisphere_split():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            CASE WHEN latitude >= 0 THEN 'North' ELSE 'South' END AS hemisphere,
            COUNT(*) AS users
        FROM users
        WHERE latitude IS NOT NULL
        GROUP BY hemisphere
    """)

    for row in cur.fetchall():
        print(row)

    conn.close()

def geo_outliers():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        SELECT user_id, city, latitude, longitude
        FROM users
        WHERE latitude NOT BETWEEN -90 AND 90
           OR longitude NOT BETWEEN -180 AND 180
    """)

    for row in cur.fetchall():
        print(row)

    conn.close()
def cities_missing_geo():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        SELECT city, COUNT(*) AS missing
        FROM users
        WHERE latitude IS NULL OR longitude IS NULL
        GROUP BY city
        ORDER BY missing DESC
    """)

    for row in cur.fetchall():
        print(row)

    conn.close()

def city_geo_spread():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        SELECT city,
               MAX(latitude) - MIN(latitude) AS lat_spread,
               MAX(longitude) - MIN(longitude) AS lon_spread
        FROM users
        WHERE latitude IS NOT NULL
        GROUP BY city
        ORDER BY lat_spread DESC
    """)

    for row in cur.fetchall():
        print(row)

    conn.close()

def geo_insights():
    print("\nUsers per city")
    users_per_city()

    print("\nUsers by geo bucket")
    users_by_geo_bucket()

    print("\nUser density")
    user_density()

    print("\nGeo coverage")
    geo_coverage()

    print("\nHemisphere split")
    hemisphere_split()



if __name__ == "__main__":
    print("\nUsers per city")
    users_per_city()

    print("\nGeo coverage")
    geo_coverage()

    print("\nHemisphere split")
    hemisphere_split()

    print("\n geo insights")
    geo_insights()





