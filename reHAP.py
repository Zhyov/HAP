from hap.language import LanguageManager, loadLanguages
from hap.window import Window
from hap.loader import loadCharacters, loadAlphabetsManifest
from hap.config import loadConfig, CONFIG_PATH

def loadSetup(manager):
    # [Languages]

    from hap.window import Letter
    manifest = loadAlphabetsManifest()
    checkOptions = []
    for alphabet in manifest:
        characters =  loadCharacters(alphabet["file"])
        languageWindow = Window(
            [{"text": "".join([character["char"].upper(), character["char"]]) if character["upper"] else character["char"], "command": lambda char=character: Letter([], manager, char).load()} for character in characters.values()],
            [], manager, "whatCharacter", autoTranslate=False
        )
        checkOptions.append({"text": alphabet["name"], "command": lambda window=languageWindow: window.load()})

    # [Main Windows]

    check = Window(checkOptions, [], manager, "whatCheck")

    language = Window(manager.getLanguages(), [], manager, "selectLanguage")
 
    settings = Window([
        {"text": "settingsLanguage", "command": lambda: language.load()}
    ], [], manager, "whatDo")

    menu = Window([
        {"text": "menuCheck", "command": lambda: check.load()},
        {"text": "menuSettings", "command": lambda: settings.load()},
        {"text": "exit", "command": lambda: exit()}
    ], [], manager, "whatDo", welcome=True)

    return menu

if __name__ == "__main__":
    # [Load config and initialize language manager]
    config = loadConfig()
    manager = LanguageManager(config.get("language", "en"), loadLanguages(), CONFIG_PATH)

    # [Build UI]
    menu = loadSetup(manager)

    # [Start application]
    menu.load()