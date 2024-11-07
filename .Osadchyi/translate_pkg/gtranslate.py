from googletrans import Translator

translator = Translator()

LANGUAGES = {
    "af": "afrikaans",
    "sq": "albanian",
    "am": "amharic",
    "ar": "arabic",
    "hy": "armenian",
    "az": "azerbaijani",
    "eu": "basque",
    "be": "belarusian",
    "bn": "bengali",
    "en": "english",
    "fr": "french",
    "uk": "ukrainian",
}


def TransLate(text: str, scr: str = 'auto', dest: str = 'en') -> str:
    try:
        if scr == 'auto':
            scr = translator.detect(text).lang
        translated_text = translator.translate(text, src=scr, dest=dest).text
        return translated_text
    except Exception as e:
        return f"Error: {e}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        detection = translator.detect(text)
        lang = detection.lang
        confidence = detection.confidence
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
        if lang in LANGUAGES.values():
            return list(LANGUAGES.keys())[list(LANGUAGES.values()).index(lang)]
        elif lang in LANGUAGES.keys():
            return LANGUAGES[lang]
        else:
            return "Error: Language not found"
    except Exception as e:
        return f"Error: {e}"


def LanguageList(out: str = "screen", text: str = None) -> str:
    # Define column widths for consistent formatting
    col_widths = [4, 15, 12, 30]

    output = (
            f"{'N'.ljust(col_widths[0])}"
            f"{'Language'.ljust(col_widths[1])}"
            f"{'ISO-639 code'.ljust(col_widths[2])}"
            f"{'Text'.ljust(col_widths[3])}\n"
            + "-" * sum(col_widths) + "\n"
    )

    try:
        for idx, (code, lang) in enumerate(LANGUAGES.items(), start=1):
            translated_text = translator.translate(text, dest=code).text if text else ""
            output += (
                f"{str(idx).ljust(col_widths[0])}"
                f"{lang.ljust(col_widths[1])}"
                f"{code.ljust(col_widths[2])}"
                f"{translated_text.ljust(col_widths[3])}\n"
            )

        if out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as file:
                file.write(output)
            return "Ok"
        else:
            print(output)
            return "Ok"
    except Exception as e:
        return f"Error: {e}"
