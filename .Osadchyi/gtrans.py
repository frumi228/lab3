from translate_pkg.gtranslate import TransLate, LangDetect, CodeLang, LanguageList

print(TransLate("Hello", "uk", "en"))
print(LangDetect("Hello", "all"))
print(CodeLang("en"))
print(LanguageList("file", "Have nice day"))
