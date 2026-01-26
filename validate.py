# validate.py
import logging

def validate_users(users):
    valid = []
    seen_ids = set()

    for u in users:
        if u["user_id"] in seen_ids:
            logging.warning(f"Duplicate user_id rejected: {u}")
            continue

        if "@" not in u["email"]:
            logging.warning(f"Invalid email rejected: {u}")
            continue

        if not u["city"]:
            logging.warning(f"City null rejected: {u}")
            continue

        if not u["zipcode"] or len(u["zipcode"]) < 5:
            logging.warning(f"Invalid zipcode rejected: {u}")
            continue

        seen_ids.add(u["user_id"])
        valid.append(u)

    logging.info(f"Validated users count: {len(valid)}")
    return valid
