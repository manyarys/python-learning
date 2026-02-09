# CSV Cleaner

Small Python tool to clean contact lists (CSV).

## What it does
- normalizes phone numbers (keeps digits only)
- removes duplicates (by email, otherwise by phone)
- exports cleaned CSV + prints a report

## Run
```bash
cd projects/csv_cleaner
python app.py
