from hap.language import LanguageManager, loadLanguages
from hap.window import Window
from hap.loader import loadCharacters
from hap.config import loadConfig, CONFIG_PATH

def loadSetup(manager):
    # [Languages]

    spanishCharacters = loadCharacters("spanish.json")
    russianCharacters = loadCharacters("russian.json")

    from hap.window import Letter
    spanish = Window(
        [{"text": character["char"], "command": lambda char=character: Letter([], manager, char).load()} for character in spanishCharacters.values()],
        [], manager, manager.getText("whatCharacter")
    )

    russian = Window(
        [{"text": character["char"], "command": lambda char=character: Letter([], manager, char).load()} for character in russianCharacters.values()],
        [], manager, manager.getText("whatCharacter")
    )

    # [Main Windows]

    check = Window([
        {"text": manager.getText("spanish"), "command": lambda: spanish.load()},
        {"text": manager.getText("russian"), "command": lambda: russian.load()}
    ], [], manager, manager.getText("whatCheck"))

    language = Window(manager.getLanguages(), [], manager, manager.getText("selectLanguage"))
 
    settings = Window([
        {"text": manager.getText("settingsLanguage"), "command": lambda: language.load()}
    ], [], manager, manager.getText("whatDo"))

    menu = Window([
        {"text": manager.getText("menuCheck"), "command": lambda: check.load()},
        {"text": manager.getText("menuSettings"), "command": lambda: settings.load()},
        {"text": manager.getText("exit"), "command": lambda: exit()}
    ], [], manager, manager.getText("whatDo"), "", True)

    return menu

if __name__ == "__main__":
    # [Load config and initialize language manager]
    config = loadConfig()
    manager = LanguageManager(config.get("language", "en"), loadLanguages(), CONFIG_PATH)

    # [Build UI]
    menu = loadSetup(manager)

    # [Start application]
    menu.load()