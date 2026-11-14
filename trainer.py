"""Режим тренировки: проверка перевода."""
import random

from dictionary import normalize
from ui import ask_int


def run_training(words):
    """Тренировка. Коллекции: list (случайный порядок вопросов),
    set (слова, в которых были ошибки)."""
    if not words:
        print("Словарь пуст — добавьте слова для тренировки.")
        return
    count = ask_int(f"Сколько слов проверить (1-{len(words)})? ", 1, len(words))
    if count is None:
        return
    questions = random.sample(list(words.items()), count)
    mistakes = set()
    correct = 0
    print("Переведите слово (пустая строка — завершить досрочно).")
    asked = 0
    for word, translation in questions:
        answer = input(f"  {word} -> ")
        if not answer.strip():
            break
        asked += 1
        if normalize(answer) == translation:
            correct += 1
            print("  Верно!")
        else:
            mistakes.add(word)
            print(f"  Неверно. Правильно: {translation}")
    print(f"\nРезультат: {correct} из {asked}.")
    if mistakes:
        print("Повторите слова: " + ", ".join(sorted(mistakes)))
