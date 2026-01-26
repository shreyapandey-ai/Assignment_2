# transform.py
import logging

def transform_users(raw_users):
    cleaned = []

    for user in raw_users:
        cleaned.append({
            "user_id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": user.get("address", {}).get("city"),
            "zipcode": user.get("address", {}).get("zipcode")
        })

    logging.info("Data transformed successfully")
    return cleaned
