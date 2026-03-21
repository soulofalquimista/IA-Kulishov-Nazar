def count_vowels():
    text = input("Введіть рядок: ")
    vowels = "aeiouAEIOUаеєиіїоуюяАЕЄИІЇОУЮЯ"
    count = sum(1 for char in text if char in vowels)
    print("Кількість голосних:", count)


def check_palindrome():
    text = input("Введіть рядок: ")
    cleaned = text.replace(" ", "").lower()
    if cleaned == cleaned[::-1]:
        print("Це паліндром")
    else:
        print("Це НЕ паліндром")


def replace_spaces():
    text = input("Введіть рядок: ")
    print("Результат:", text.replace(" ", "_"))


def sort_strings():
    words = input("Введіть слова через пробіл: ").split()
    words.sort()
    print("Відсортовано:", words)


while True:
    print("\n=== МЕНЮ ===")
    print("1 — Порахувати голосні")
    print("2 — Перевірити паліндром")
    print("3 — Замінити пробіли на _")
    print("4 — Сортувати слова")
    print("0 — Вихід")

    choice = input("Оберіть дію: ")

    if choice == "1":
        count_vowels()
    elif choice == "2":
        check_palindrome()
    elif choice == "3":
        replace_spaces()
    elif choice == "4":
        sort_strings()
    elif choice == "0":
        print("Програму завершено.")
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")
