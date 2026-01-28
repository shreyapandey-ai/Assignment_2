import os
import csv
import logging

from extract import extract_users
from transform import transform_users
from validate import validate_users
from load_sqlite import load_to_sqlite


# create folders if missing
os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)

# logging setup
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def save_csv(users):
    if not users:
        return

    fieldnames = set()
    for u in users:
        fieldnames.update(u.keys())

    with open("data/cleaned_users.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=sorted(fieldnames)
        )
        writer.writeheader()
        writer.writerows(users)


# 🔽 PIPELINE EXECUTION
raw = extract_users()
cleaned = transform_users(raw)
validated = validate_users(cleaned)

save_csv(validated)
load_to_sqlite(validated)


print("Pipeline completed successfully");

