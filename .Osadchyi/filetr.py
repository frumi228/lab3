import json
import os
import re
from translate_pkg.gtranslate import TransLate


def read_config(config_file):
    try:
        with open(config_file, 'r', encoding='utf-8') as file:
            config = json.load(file)
        return config
    except Exception as e:
        print(f"Помилка читання конфігураційного файлу: {e}")
        return None


def read_text_file(text_file, max_chars, max_words, max_sentences):
    try:
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Розрахунок характеристик тексту
        char_count = len(text)
        word_count = len(text.split())
        sentence_count = len(re.split(r'[.!?]', text)) - 1

        print(f"Назва файлу: {text_file}")
        print(f"Розмір файлу: {os.path.getsize(text_file)} байтів")
        print(f"Кількість символів: {char_count}")
        print(f"Кількість слів: {word_count}")
        print(f"Кількість речень: {sentence_count}")

        if char_count > max_chars:
            text = text[:max_chars]
        if word_count > max_words:
            text = ' '.join(text.split()[:max_words])
        if sentence_count > max_sentences:
            sentences = re.split(r'(?<=[.!?]) +', text)[:max_sentences]
            text = ' '.join(sentences)

        return text
    except FileNotFoundError:
        print("Помилка: Текстовий файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка читання текстового файлу: {e}")
        return None


def main():
    # Читаємо конфігураційний файл
    config = read_config('config.json')
    if not config:
        return

    text_file = config.get("text_file")
    target_language = config.get("target_language")
    output = config.get("output")
    max_chars = config.get("max_chars", 600)
    max_words = config.get("max_words", 100)
    max_sentences = config.get("max_sentences", 5)

    # Читаємо текст із файлу з урахуванням обмежень
    text = read_text_file(text_file, max_chars, max_words, max_sentences)
    if not text:
        return

    # Перекладаємо текст
    translated_text = TransLate(text, dest=target_language)
    if "Error" in translated_text:
        print(f"Помилка перекладу: {translated_text}")
        return

    # Вивід результату
    if output == "screen":
        print(f"Перекладено на {target_language}:")
        print(translated_text)
    elif output == "file":
        output_file = f"{os.path.splitext(text_file)[0]}_{target_language}.txt"
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(translated_text)
            print("Успішно збережено у файл.")
        except Exception as e:
            print(f"Помилка запису у файл: {e}")


if __name__ == "__main__":
    main()
