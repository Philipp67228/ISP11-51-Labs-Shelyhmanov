"""Работа с файлом данных (JSON): загрузка и сохранение словаря."""
import json
import os


def load_words(path):
    """Читает словарь {слово: перевод} из файла.

    Если файла нет — возвращает пустой словарь.
    Если файл повреждён — сохраняет копию .bak и возвращает пустой словарь.
    """
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("ожидался объект JSON {слово: перевод}")
        # оставляем только корректные пары строка -> строка
        return {str(k): str(v) for k, v in data.items() if str(k).strip() and str(v).strip()}
    except (json.JSONDecodeError, ValueError) as e:
        print(f"[!] Файл данных повреждён ({e}). Начинаем с пустого словаря.")
        try:
            os.replace(path, path + ".bak")
            print(f"    Копия повреждённого файла: {path}.bak")
        except OSError:
            pass
        return {}
    except OSError as e:
        print(f"[!] Не удалось прочитать файл: {e}. Начинаем с пустого словаря.")
        return {}


def save_words(path, words):
    """Записывает словарь в файл. Возвращает True при успехе."""
    tmp = path + ".tmp"
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(words, f, ensure_ascii=False, indent=2, sort_keys=True)
        os.replace(tmp, path)  # атомарная замена, чтобы не потерять данные
        return True
    except OSError as e:
        print(f"[!] Ошибка записи файла: {e}")
        return False
