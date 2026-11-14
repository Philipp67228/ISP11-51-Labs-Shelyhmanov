"""Консольный интерфейс: меню и безопасный ввод."""

MENU = """
=== Словарь иностранных слов ===
1. Показать все слова
2. Добавить слово
3. Найти слово
4. Удалить слово
5. Тренировка
0. Сохранить и выйти
"""


def show_menu():
    print(MENU)
    return input("Выберите пункт: ").strip()


def ask_int(prompt, low, high):
    """Запрашивает целое число в диапазоне. При неверном вводе — повтор, пустая строка — отмена."""
    while True:
        raw = input(prompt).strip()
        if not raw:
            return None
        try:
            value = int(raw)
        except ValueError:
            print("Нужно ввести целое число.")
            continue
        if low <= value <= high:
            return value
        print(f"Число должно быть от {low} до {high}.")


def print_words(items):
    """Печатает список пар в виде таблицы."""
    if not items:
        print("Ничего не найдено.")
        return
    width = max(len(w) for w, _ in items)
    for i, (w, t) in enumerate(items, 1):
        print(f"{i:>3}. {w:<{width}} — {t}")
    print(f"Всего: {len(items)}")
