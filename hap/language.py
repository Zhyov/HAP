import json, os

class Language:
    def __init__(self, name: str, key: str, code: str, translations: dict):
        self.name = name
        self.code = code
        self.key = key
        self.translations = translations

    def getText(self, identifier: str):
        return self.translations.get(identifier, " ".join([self.translations.get("noTranslationText"), identifier]))

    def getCode(self): return self.code

    def getName(self): return self.name

    def getKey(self): return self.key

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

    def getText(self, identifier: str):
        return self.languages.get(self.currentLanguage).getText(identifier)

    def getLanguages(self):
        # Return a list with the name of the language and a lambda function to the language
        return [{"text": language.getKey(), "command": (lambda code=language.getCode(): self.setLanguage(code))} for language in self.languages.values()]

def loadLanguagesManifest():
    base = os.path.join(os.path.dirname(__file__), "data", "translations")
    with open(os.path.join(base, "manifest.json"), "r", encoding="utf-8") as f:
        return json.load(f)

def loadLanguages():
    base = os.path.join(os.path.dirname(__file__), "data", "translations")
    manifest = loadLanguagesManifest()
    languages = {}
    for language in manifest:
        with open(os.path.join(base, language["file"]), "r", encoding="utf-8") as f:
            languages[language["code"]] = Language(language["name"], language["key"], language["code"], json.load(f))
    return languages