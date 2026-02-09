import csv
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

INPUT_FILE = BASE_DIR / "sample_contacts.csv"
OUTPUT_FILE = BASE_DIR / "contacts_clean.csv"


def normalize_phone(phone: str) -> str:
    if not phone:
        return ""
    digits = re.sub(r"\D", "", phone)
    return digits


def load_contacts(path: Path):
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def save_contacts(path: Path, rows, fieldnames):
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    if not INPUT_FILE.exists():
        print(f"Файл не найден: {INPUT_FILE}")
        return

    rows = load_contacts(INPUT_FILE)
    total = len(rows)

    cleaned = []
    seen = set()

    for row in rows:
        email = (row.get("email") or "").strip().lower()
        phone_raw = (row.get("phone") or "").strip()
        phone_norm = normalize_phone(phone_raw)

        # выбираем ключ дедупликации: email приоритетнее, иначе phone
        key = None
        if email:
            key = ("email", email)
        elif phone_norm:
            key = ("phone", phone_norm)
        else:
            # если нет ни email ни телефона — оставим, но пометим уникальным ключом по индексу
            key = ("row", len(cleaned))

        if key in seen:
            continue
        seen.add(key)

        row["phone"] = phone_norm
        cleaned.append(row)

    removed = total - len(cleaned)

    fieldnames = list(rows[0].keys()) if rows else ["name", "phone", "email", "city"]
    save_contacts(OUTPUT_FILE, cleaned, fieldnames)

    print("=== CSV Cleaner Report ===")
    print(f"Input rows: {total}")
    print(f"Unique rows: {len(cleaned)}")
    print(f"Duplicates removed: {removed}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
