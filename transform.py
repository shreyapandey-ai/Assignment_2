# transform.py
import logging
from geocode import geocode

def transform_users(raw_users):
        cleaned = []

        for user in raw_users:
           lat, lon = geocode(
           user.get("address", {}).get("city"),
         user.get("address", {}).get("zipcode")
          )
        
           cleaned.append({
                "user_id": user.get("id"),
               "name": user.get("name"),
                 "email": user.get("email"),
                 "city": user.get("address", {}).get("city"),
                  "zipcode": user.get("address", {}).get("zipcode"),
                   "latitude": lat,
                    "longitude": lon


        })

        logging.info("Data transformed successfully")
        return cleaned
