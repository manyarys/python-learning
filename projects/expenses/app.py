from storage import load_data, save_expense, reset_file

totals_by_category = {}


def print_report():
    print("\nОтчёт по категориям:")
    if not totals_by_category:
        print("Пока нет расходов.\n")
        return

    grand_total = 0
    for category, amount in sorted(totals_by_category.items()):
        print(f"- {category}: {amount:.2f}")
        grand_total += amount

    print(f"\nИТОГО: {grand_total:.2f}\n")


def top_category():
    if not totals_by_category:
        print("Пока нет расходов.\n")
        return
    category, amount = max(totals_by_category.items(), key=lambda x: x[1])
    print(f"Топ категория: {category} = {amount:.2f}\n")


def reset_data():
    confirm = input("Точно очистить ВСЕ данные? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Отменено.\n")
        return

    reset_file()
    totals_by_category.clear()
    print("Данные очищены.\n")


def is_number(value: str) -> bool:
    value = value.strip()
    if value.count(".") > 1:
        return False
    return value.replace(".", "", 1).isdigit()


# загружаем данные ИЗ storage
load_data(totals_by_category)

print("Учёт расходов (модульная версия)")
print("Формат ввода: категория сумма")
print("Пример: food 12.50")
print("Команды: report | top | reset | q\n")

print_report()

while True:
    text = input("Ввод: ").strip()
    cmd = text.lower()

    if cmd == "q":
        break

    if cmd == "report":
        print_report()
        continue

    if cmd == "top":
        top_category()
        continue

    if cmd == "reset":
        reset_data()
        continue

    parts = text.split()
    if len(parts) != 2:
        print("Нужно: категория сумма (например: food 12.50)\n")
        continue

    category = parts[0].strip().lower()
    amount_str = parts[1].strip()

    if not is_number(amount_str):
        print("Сумма должна быть числом.\n")
        continue

    amount = float(amount_str)

    save_expense(category, amount)
    totals_by_category[category] = totals_by_category.get(category, 0) + amount
    print(f"Добавлено: {category} {amount:.2f}\n")

print_report()
print("Пока!")
