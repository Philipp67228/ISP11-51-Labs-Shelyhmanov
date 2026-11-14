"""Точка входа: консольный словарь иностранных слов."""
import os

import dictionary
import storage
import trainer
import ui

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "words.json")
DATA_FILE = os.path.normpath(DATA_FILE)


def handle_add(words):
    word = input("Слово: ")
    translation = input("Перевод: ")
    status = dictionary.add_word(words, word, translation)
    messages = {
        "added": "Слово добавлено.",
        "updated": "Слово уже было — перевод обновлён.",
        "empty": "Слово и перевод не могут быть пустыми.",
    }
    print(messages[status])
    return status != "empty"


def handle_remove(words):
    if dictionary.remove_word(words, input("Какое слово удалить: ")):
        print("Слово удалено.")
        return True
    print("Такого слова нет.")
    return False


def handle_search(words):
    ui.print_words(dictionary.find_words(words, input("Что искать (слово или перевод): ")))


def main():
    words = storage.load_words(DATA_FILE)
    print(f"Загружено слов: {len(words)}")
    try:
        while True:
            choice = ui.show_menu()
            changed = False
            if choice == "1":
                ui.print_words(dictionary.sorted_items(words))
            elif choice == "2":
                changed = handle_add(words)
            elif choice == "3":
                handle_search(words)
            elif choice == "4":
                changed = handle_remove(words)
            elif choice == "5":
                trainer.run_training(words)
            elif choice == "0":
                break
            else:
                print("Нет такого пункта меню.")
            if changed:
                storage.save_words(DATA_FILE, words)
    except (KeyboardInterrupt, EOFError):
        print()
    if storage.save_words(DATA_FILE, words):
        print("Данные сохранены. До свидания!")


if __name__ == "__main__":
    main()
