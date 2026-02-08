total = 0

while True:
    value = input("Введи число (или 'q' для выхода): ")

    if value == "q":
        break

    if not value.isdigit():
        print("Это не число, попробуй ещё раз.")
        continue

    total += int(value)
    print(f"Текущая сумма: {total}")

print(f"Итоговая сумма: {total}")
