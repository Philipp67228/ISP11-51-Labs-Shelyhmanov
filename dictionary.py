"""Операции со словарём в памяти. Коллекция: dict {слово: перевод}."""


def normalize(text):
    """Приводит строку к единому виду (без пробелов по краям, в нижнем регистре)."""
    return text.strip().lower()


def add_word(words, word, translation):
    """Добавляет пару. Возвращает 'added', 'updated' или 'empty'."""
    word, translation = normalize(word), normalize(translation)
    if not word or not translation:
        return "empty"
    status = "updated" if word in words else "added"
    words[word] = translation
    return status


def remove_word(words, word):
    """Удаляет слово. Возвращает True, если оно было в словаре."""
    return words.pop(normalize(word), None) is not None


def find_words(words, query):
    """Ищет по подстроке в слове или переводе. Возвращает список пар."""
    q = normalize(query)
    if not q:
        return []
    return [(w, t) for w, t in sorted(words.items()) if q in w or q in t]


def sorted_items(words):
    """Все пары, отсортированные по слову."""
    return sorted(words.items())
