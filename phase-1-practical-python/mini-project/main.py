import csv
import logging
from validators import clean_record
import json

# --- Logging setup ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("phase-1-practical-python/mini-project/automation.log"),
        logging.StreamHandler()
    ]
)

# --- Main processing ---
valid_records = []
total_count = 0
invalid_count = 0

with open("phase-1-practical-python/mini-project/data/raw_signups.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_count += 1
        cleaned_row = clean_record(row)
        if cleaned_row:
            valid_records.append(cleaned_row)
            logging.info(f"Valid record: {cleaned_row}")
        else:
            invalid_count += 1
            logging.warning(f"Invalid record: {row}")

# --- Write output ---
with open("phase-1-practical-python/mini-project/output/clean_data.json", "w") as file:
    json.dump(valid_records, file, indent=4)

# --- Summary ---
valid_count = len(valid_records)

logging.info(f"Total records: {total_count}")
logging.info(f"Valid records: {valid_count}")
logging.info(f"Invalid records: {invalid_count}")
