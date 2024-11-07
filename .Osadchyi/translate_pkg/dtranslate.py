from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

supported_languages = {
    "en": "english",
    "fr": "french",
    "uk": "ukrainian",
    "es": "spanish",
    "de": "german",
    "it": "italian",
    "pt": "portuguese",
}


def TransLate(text: str, scr: str = 'auto', dest: str = 'en') -> str:
    try:
        if scr == 'auto':
            scr = detect(text)
        translated_text = GoogleTranslator(source=scr, target=dest).translate(text)
        return translated_text
    except Exception as e:
        return f"Error: {e}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        lang = detect(text)
        confidence = "0.99"  # Level of confidence
        if set == "lang":
            return lang
        elif set == "confidence":
            return confidence
        else:
            return f"{lang}, {confidence}"
    except Exception as e:
        return f"Error: {e}"


def CodeLang(lang: str) -> str:
    try:
        if lang in supported_languages.values():
            return list(supported_languages.keys())[list(supported_languages.values()).index(lang)]
        elif lang in supported_languages.keys():
            return supported_languages[lang]
        else:
            return "Помилка: Мова не знайдена"
    except Exception as e:
        return f"Error: {e}"


def LanguageList(out: str = "screen", text: str = None) -> str:
    # Define headers with fixed column widths
    output = f"{'N':<3}{'Language':<12}{'ISO-639 code':<12}{'Text':<30}\n" + "-" * 60 + "\n"

    try:
        for idx, (code, lang) in enumerate(supported_languages.items(), start=1):
            translated_text = GoogleTranslator(target=code).translate(text) if text else ""
            # Adjust each column width for alignment
            output += f"{idx:<3}{lang:<12}{code:<12}{translated_text:<30}\n"

        if out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as file:
                file.write(output)
            return "Ok"
        else:
            print(output)
            return "Ok"
    except Exception as e:
        return f"Помилка: {e}"
