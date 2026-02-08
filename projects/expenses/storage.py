FILENAME = "expenses_v3.txt"

def load_data(totals_by_category):
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",", 1)
                if len(parts) != 2:
                    continue

                category = parts[0].strip().lower()
                amount = float(parts[1].strip())

                totals_by_category[category] = totals_by_category.get(category, 0) + amount
    except FileNotFoundError:
        pass


def save_expense(category, amount):
    with open(FILENAME, "a") as file:
        file.write(f"{category},{amount}\n")


def reset_file():
    with open(FILENAME, "w") as file:
        file.write("")
