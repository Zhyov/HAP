import json, os

class Language:
    def __init__(self, name: str, code: str, translations: dict):
        self.name = name
        self.code = code
        self.translations = translations

    def getText(self, identifier: str):
        return self.translations.get(identifier)

    def getCode(self): return self.code

    def getName(self): return self.name

class LanguageManager:
    def __init__(self, currentLanguage, languages: dict, configPath = None):
        self.currentLanguage = currentLanguage
        self.languages = languages
        self.configPath = configPath

    def setLanguage(self, code: str):
        self.currentLanguage = code

        # Save to config if path provided
        if self.configPath:
            os.makedirs(os.path.dirname(self.configPath), exist_ok=True)
            with open(self.configPath, "w", encoding="utf-8") as f:
                json.dump({"language": code}, f, indent=4, ensure_ascii=False)

        # Reload UI
        from reHAP import loadSetup
        menu = loadSetup(self)
        menu.load()

    def getText(self, identifier: str):
        return self.languages.get(self.currentLanguage).getText(identifier)

    def getLanguages(self):
        # Return a list with the name of the language and a lambda function to the language
        return [{"text": language.getName(), "command": (lambda code=language.getCode(): self.setLanguage(code))} for language in self.languages.values()]

def loadLanguages():
    base = os.path.join(os.path.dirname(__file__), "data")
    with open(f"{base}/english.json", "r", encoding="utf-8") as f:
        en = Language("English", "en", json.load(f))
    with open(f"{base}/spanish.json", "r", encoding="utf-8") as f:
        es = Language("Español", "es", json.load(f))
    return {"en": en, "es": es}