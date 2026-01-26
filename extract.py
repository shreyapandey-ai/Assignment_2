# extract.py
import requests
import json
import logging
import os

URL = "https://jsonplaceholder.typicode.com/users"

def extract_users():
    try:
        os.makedirs("data", exist_ok=True)   # 👈 AUTO CREATE FOLDER

        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        with open("data/raw_users.json", "w") as f:
            json.dump(data, f, indent=4)

        logging.info("Data extracted successfully")
        return data

    except requests.exceptions.RequestException as e:
        logging.error(f"API failed: {e}")
        return []
