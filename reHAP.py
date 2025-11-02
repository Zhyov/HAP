# [Imports]

import os

# [Constants]

VER = "v0.7"
SELECT = ">> "
WELCOMEMSG = f"""

██████╗ ███████╗██╗  ██╗ █████╗ ██████╗
██╔══██╗██╔════╝██║  ██║██╔══██╗██╔══██╗
██████╔╝█████╗  ███████║███████║██████╔╝
██╔══██╗██╔══╝  ██╔══██║██╔══██║██╔═══╝
██║  ██║███████╗██║  ██║██║  ██║██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     {VER}
"""

# X-SAMPA to IPA mapping
IPA = {
    " ": "",  # Silent character

    # [Vowels]
    "i": "i",
    "y": "y",
    "1": "ɨ",
    "}": "ʉ",
    "M": "ɯ",
    "u": "u",
    "I": "ɪ",
    "Y": "ʏ",
    "U": "ʊ",
    "e": "e",
    "2": "ø",
    "@\\": "ɘ",
    "8": "ɵ",
    "7": "ɤ",
    "o": "o",
    "e_o": "e̞",
    "E_r": "ɛ̝",
    "2_o": "ø̞",
    "9_r": "œ̝",
    "@": "ə",
    "E": "ɛ",
    "9": "œ",
    "3": "ɜ",
    "3\\": "ɞ",
    "V": "ʌ",
    "O": "ɔ",
    "{": "æ",
    "6": "ɐ",
    "a": "a",
    "&": "ɶ",
    "a_\"": "ä",
    "A": "ɑ",
    "Q": "ɒ",

    # [Consonants]
    "m": "m",
    "n": "n",
    "J": "ɲ",
    "N": "ŋ",
    "p": "p",
    "b": "b",
    "t": "t",
    "d": "d",
    "c": "c",
    "J\\": "ɟ",
    "k": "k",
    "g": "g",
    "q": "q",
    "G\\": "ɢ",
    "?": "ʔ",
    "s": "s",
    "z": "z",
    "S": "ʃ",
    "Z": "ʒ",
    "s`": "ʂ",
    "z`": "ʐ",
    "s\\": "ɕ",
    "z\\": "ʑ",
    "p\\": "ɸ",
    "B": "β",
    "f": "f",
    "v": "v",
    "T": "θ",
    "D": "ð",
    "C": "ç",
    "j\\": "ʝ",
    "x": "x",
    "G": "ɣ",
    "X": "χ",
    "R": "ʁ",
    "h": "h",
    "r\\": "ɹ",
    "j": "j",
    "M\\": "ɰ",
    "4": "ɾ",
    "r": "r",
    "R\\": "ʀ",
    "K": "ɬ",
    "K\\": "ɮ",
    "l": "l",
    "5": "ɫ",
    "L": "ʎ",

    # [Other Symbols]
    "_j": "ʲ",
    ":": "ː",
}

# [Variables]

windowStack = []

# [Global Functions]

# Clear screen based on OS
if os.name == "nt":
    def clearScreen(): os.system("cls")
else:
    def clearScreen(): os.system("clear")

def handleInformation(pretext, information):
    if pretext is not None: print(pretext)

    # Iterate and print all texts
    for text in information:
        print(text)

def handleSelection(posttext, options):
    print() # Blank line for spacing

    # Iterate and print all options
    for index, option in enumerate(options, start=1):
        print(f"{index}) {option['text']}")
    
    if posttext is not None: print(posttext)

def handleOption(selected, options):
    try:
        selected = int(selected) - 1

        # Check if selected is within range
        if 0 <= selected < len(options):
            # Run lambda function
            options[selected].get("command", lambda: None)()
    except ValueError:
        pass

def separateXSAMPA(codes):
    result = ""
    code = codes.split("-")
    for xsampa in code: result += IPA[xsampa]
    return result

def loadIPA(IPACodes):
    result = []
    for IPACode in IPACodes:
        IPAInfo = f" ({IPACode['info']})" if IPACode['info'] is not None else ""
        result.append(f"{separateXSAMPA(IPACode['xsampa'])}{IPAInfo}")
    return ", ".join(result)

def loadChar(charInfo, reduced: bool = False):
    if reduced: print(f"{manager.getText('variationEffect')}: {charInfo['change']}")
    else:
        char = charInfo['char'].upper() if charInfo['upper'] else ""
        print(f"{manager.getText('charText')}: {char if not reduced else ''}{charInfo['char']}")
        if charInfo['native'] is not None: print(f"{manager.getText('charName')}: {charInfo['native']}")
    print(f"{manager.getText('charIPA')}: {loadIPA(charInfo['ipa'])}")

# [Classes]

class Window:
    def __init__(self, options: list, information: list = [], pretext: str = "", posttext: str = "", welcome: bool = False):
        self.options = options
        self.pretext = pretext
        self.posttext = posttext
        self.welcome = welcome
        self.information = information

    def load(self):
        # Keep track of last opened windows
        windowStack.append(self)

        # While this window is the current window
        while windowStack and windowStack[-1] is self:
            clearScreen()

            if self.welcome: print(WELCOMEMSG)
            handleInformation(self.pretext, self.information)

            # Create a temporary list to not modify self.options
            optionsToShow = list(self.options)

            # Automatically add the back option to the window unless its the main window
            if not self.welcome:
                from __main__ import manager
                optionsToShow.append({"text": manager.getText("back"), "command": lambda: self.close()})

            handleSelection(self.posttext, optionsToShow)
            handleOption(input(SELECT), optionsToShow)
    
    # Remove from window stack when done
    def close(self):
        if windowStack and windowStack[-1] is self:
            windowStack.pop()

class Letter(Window):
    def __init__(self, options, details: dict = {}, reduced: bool = False):
        super().__init__(options, details)
        self.details = details
        self.reduced = reduced

    def load(self):
        # Keep track of last opened windows
        windowStack.append(self)

        # While this window is the current window
        while windowStack and windowStack[-1] is self:
            clearScreen()

            loadChar(self.details, self.reduced)

            # Create a temporary list to not modify self.options
            optionsToShow = list(self.options)            
            
            # Automatically add the variations and back option to the window
            from __main__ import manager
            if self.details.get("variations"):
                optionsToShow.append({
                    "text": manager.getText("variations"),
                    "command": lambda: self.loadVariations()
                })
            optionsToShow.append({"text": manager.getText("back"), "command": lambda: self.close()})

            handleSelection(self.posttext, optionsToShow)
            handleOption(input(SELECT), optionsToShow)
    
    def loadVariations(self):
        # Get variations, return if none
        variations = self.details.get("variations", [])
        if not variations: return
        
        # Create and load variations window
        from __main__ import manager
        variationWindow = Window(
            [{"text": variation["char"], "command": lambda var=variation: Letter([], var, True).load()} for variation in variations],
            [], manager.getText("variations")
        )
        variationWindow.load()

    # Remove from window stack when done
    def close(self):
        if windowStack and windowStack[-1] is self:
            windowStack.pop()

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
    def __init__(self, currentLanguage, languages: dict):
        self.currentLanguage = currentLanguage
        self.languages = languages

    def setLanguage(self, code: str):
        global windowStack

        from __main__ import loadSetup
        self.currentLanguage = code
        windowStack = [] # Clear old windows
        loadSetup() # Reload windows with new language

        from __main__ import menu
        menu.load() # Load menu with new language

    def getText(self, identifier: str):
        return self.languages.get(self.currentLanguage).getText(identifier)

    def getLanguages(self):
        # Return a list with the name of the language and a lambda function to the language
        return [{"text": language.getName(), "command": (lambda code=language.getCode(): self.setLanguage(code))} for language in self.languages.values()]

# [Languages]

englishLanguage = Language("English", "en", {
    "whatDo": "What do you want do?",
    "whatCheck": "What language would you like to check?",
    "whatCharacter": "What character would you like to check?",
    
    "menuCheck": "Check",
    "menuSettings": "Settings",

    "charText": "Character",
    "charName": "Native Name",
    "charIPA": "IPA Pronunciation",
    "variations": "Variations",
    "variationEffect": "Change or usage",

    "settingsLanguage": "Language",
    
    "selectLanguage": "Select a language:",
    "english": "English",
    "spanish": "Spanish",
    "russian": "Russian",

    "whenSoftVowel": "when it is before an \"e\" or \"i\"",
    "whenNotFirst": "when it is not the first letter in a word",
    "whenFirst": "when it is the first letter in a word",
    "whenSilent": "it is silent",
    "whenDouble": "when it is doubled",
    "whenReal": "in real speech",
    "whenLoanword": "only used in loanwords, pronounced as in the original language",
    "whenDialect": "in certain dialects",
    "whenPalatized": "when it is palatized",
    "whenUnstressed": "when it is unstressed",

    "changeStress": "Stressed variant",
    "changeDouble": "Different pronunciation when doubled",
    "changeDigraph": "Digraph with different pronunciation",
    "changeSpanishQU": "Indication that the \"u\" is pronounced after a \"q\", only when followed by an \"e\" or \"i\"",

    "exit": "Exit",
    "back": "Back"
})

spanishLanguage = Language("Español", "es", {
    "whatDo": "¿Qué quieres hacer?",
    "whatCheck": "¿Qué idioma desea comprobar?",
    "whatCharacter": "¿Qué carácter desea comprobar?",
    
    "menuCheck": "Comprobar",
    "menuSettings": "Ajustes",
    
    "charText": "Carácter",
    "charName": "Nombre Nativo",
    "charIPA": "Pronunciación de IPA",
    "variations": "Variaciones",
    "variationEffect": "Cambio o uso",
    
    "settingsLanguage": "Idioma",
    
    "selectLanguage": "Seleccione un idioma:",
    "english": "Inglés",
    "spanish": "Español",
    "russian": "Ruso",

    "whenSoftVowel": "cuando esta antes de una \"e\" o \"i\"",
    "whenNotFirst": "cuando no es la primera letra de una palabra",
    "whenFirst": "cuando es la primera letra de una palabra",
    "whenSilent": "no se pronuncia",
    "whenDouble": "cuando se duplica",
    "whenReal": "en el habla real",
    "whenLoanword": "solo usado en palabras prestadas, pronunciado como en el idioma original",
    "whenDialect": "en ciertos dialectos",
    "whenPalatized": "cuando está palatalizado",
    "whenUnstressed": "cuando no está acentuada",

    "changeStress": "Variante acentuada",
    "changeDouble": "Pronunciación diferente cuando se duplica",
    "changeDigraph": "Digrama con pronunciación diferente",
    "changeSpanishQU": "Indicación que la \"u\" se pronuncia después de una \"q\", solo cuando va seguida de una \"e\" o \"i\"",

    "exit": "Salir",
    "back": "Volver"
})

manager = LanguageManager("en", {"en": englishLanguage, "es": spanishLanguage})

# [Window Setup Function]

def loadSetup():
    global spanish, check, language, settings, menu

    # [Language Data]

    spanishCharacters = {
        "a": {"char": "a", "native": "a", "upper": True, "ipa": [{"xsampa": "a_\"", "info": None}], "variations": [{"char": "á", "change": manager.getText("changeStress"), "ipa": [{"xsampa": "a", "info": None}]}]},
        "b": {"char": "b", "native": "be", "upper": True, "ipa": [{"xsampa": "b", "info": None}, {"xsampa": "B", "info": manager.getText("whenNotFirst")}], "variations": []},
        "c": {"char": "c", "native": "ce", "upper": True, "ipa": [{"xsampa": "k", "info": None}, {"xsampa": "s", "info": manager.getText("whenSoftVowel")}, {"xsampa": "T", "info": f"{manager.getText('whenDialect')} + {manager.getText('whenSoftVowel')}"}], "variations": [{"char": "ch", "change": manager.getText("changeDigraph"), "ipa": [{"xsampa": "t-S", "info": None}]}]},
        "d": {"char": "d", "native": "de", "upper": True, "ipa": [{"xsampa": "d", "info": None}, {"xsampa": "D", "info": manager.getText("whenSoftVowel")}], "variations": []},
        "e": {"char": "e", "native": "e", "upper": True, "ipa": [{"xsampa": "e_o", "info": None}], "variations": [{"char": "é", "change": manager.getText("changeStress"), "ipa": [{"xsampa": "e_o", "info": None}]}]},
        "f": {"char": "f", "native": "efe", "upper": True, "ipa": [{"xsampa": "f", "info": None}], "variations": []},
        "g": {"char": "g", "native": "ge", "upper": True, "ipa": [{"xsampa": "g", "info": None}, {"xsampa": "G", "info": manager.getText("whenNotFirst")}, {"xsampa": "x", "info": manager.getText("whenSoftVowel")}], "variations": []},
        "h": {"char": "h", "native": "hache", "upper": True, "ipa": [{"xsampa": " ", "info": manager.getText("whenSilent")}], "variations": []},
        "i": {"char": "i", "native": "i", "upper": True, "ipa": [{"xsampa": "i", "info": None}], "variations": [{"char": "í", "change": manager.getText("changeStress"), "ipa": [{"xsampa": "i", "info": None}]}]},
        "j": {"char": "j", "native": "jota", "upper": True, "ipa": [{"xsampa": "x", "info": None}], "variations": []},
        "k": {"char": "k", "native": "ka", "upper": True, "ipa": [{"xsampa": "k", "info": None}], "variations": []},
        "l": {"char": "l", "native": "ele", "upper": True, "ipa": [{"xsampa": "l", "info": None}], "variations": [{"char": "ll", "change": manager.getText("changeDouble"), "ipa": [{"xsampa": "L", "info": None}, {"xsampa": "S", "info": manager.getText('whenDialect')}]}]},
        "m": {"char": "m", "native": "eme", "upper": True, "ipa": [{"xsampa": "m", "info": None}], "variations": []},
        "n": {"char": "n", "native": "ene", "upper": True, "ipa": [{"xsampa": "n", "info": None}], "variations": []},
        "ñ": {"char": "ñ", "native": "eñe", "upper": True, "ipa": [{"xsampa": "J", "info": None}], "variations": []},
        "o": {"char": "o", "native": "o", "upper": True, "ipa": [{"xsampa": "o", "info": None}], "variations": [{"char": "ó", "change": manager.getText("changeStress"), "ipa": [{"xsampa": "o", "info": None}]}]},
        "p": {"char": "p", "native": "pe", "upper": True, "ipa": [{"xsampa": "p", "info": None}], "variations": []},
        "q": {"char": "q", "native": "qü", "upper": True, "ipa": [{"xsampa": "k", "info": None}], "variations": []},
        "r": {"char": "r", "native": "erre", "upper": True, "ipa": [{"xsampa": "4", "info": None}, {"xsampa": "r", "info": manager.getText("whenDouble")}], "variations": []},
        "s": {"char": "s", "native": "ese", "upper": True, "ipa": [{"xsampa": "s", "info": None}, {"xsampa": "T", "info": manager.getText("whenDialect")}], "variations": []},
        "t": {"char": "t", "native": "te", "upper": True, "ipa": [{"xsampa": "t", "info": None}], "variations": []},
        "u": {"char": "u", "native": "u", "upper": True, "ipa": [{"xsampa": "u", "info": None}], "variations": [{"char": "ú", "change": manager.getText("changeStress"), "ipa": [{"xsampa": "u", "info": None}]}, {"char": "ü", "change": manager.getText("changeSpanishQU"), "ipa": [{"xsampa": "u", "info": None}]}]},
        "v": {"char": "v", "native": "ve", "upper": True, "ipa": [{"xsampa": "v", "info": None}, {"xsampa": "b", "info": manager.getText("whenReal")}], "variations": []},
        "w": {"char": "w", "native": "doble ve", "upper": True, "ipa": [{"xsampa": "u", "info": manager.getText("whenLoanword")}], "variations": []},
        "x": {"char": "x", "native": "equis", "upper": True, "ipa": [{"xsampa": "k-s", "info": None}, {"xsampa": "s", "info": manager.getText("whenFirst")}], "variations": []},
        "y": {"char": "y", "native": "i griega", "upper": True, "ipa": [{"xsampa": "j\\", "info": None}, {"xsampa": "Z", "info": manager.getText("whenDialect")}, {"xsampa": "S", "info": manager.getText("whenDialect")}], "variations": []},
        "z": {"char": "z", "native": "zeta", "upper": True, "ipa": [{"xsampa": "T", "info": None}, {"xsampa": "s", "info": manager.getText("whenDialect")}], "variations": []}
    }

    russianCharacters = {
        "а": {"char": "а", "native": "а", "upper": True, "ipa": [{"xsampa": "a", "info": None}], "variations": []},
        "b": {"char": "б", "native": "бэ", "upper": True, "ipa": [{"xsampa": "b", "info": None}], "variations": []},
        "в": {"char": "в", "native": "вэ", "upper": True, "ipa": [{"xsampa": "v", "info": None}], "variations": []},
        "г": {"char": "г", "native": "гэ", "upper": True, "ipa": [{"xsampa": "g", "info": None}], "variations": []},
        "д": {"char": "д", "native": "дэ", "upper": True, "ipa": [{"xsampa": "d", "info": None}], "variations": []},
        "е": {"char": "е", "native": "е", "upper": True, "ipa": [{"xsampa": "j-e", "info": None}, {"xsampa": "e", "info": None}], "variations": []},
        "ё": {"char": "ё", "native": "ё", "upper": True, "ipa": [{"xsampa": "j-o", "info": None}], "variations": []},
        "ж": {"char": "ж", "native": "жэ", "upper": True, "ipa": [{"xsampa": "z`", "info": None}], "variations": []},
        "з": {"char": "з", "native": "зэ", "upper": True, "ipa": [{"xsampa": "z", "info": None}], "variations": []},
        "и": {"char": "и", "native": "и", "upper": True, "ipa": [{"xsampa": "i", "info": None}], "variations": []},
        "й": {"char": "й", "native": "и краткое", "upper": True, "ipa": [{"xsampa": "j", "info": None}], "variations": []},
        "к": {"char": "к", "native": "ка", "upper": True, "ipa": [{"xsampa": "k", "info": None}], "variations": []},
        "л": {"char": "л", "native": "эль", "upper": True, "ipa": [{"xsampa": "5", "info": None}], "variations": [{"char": "ль", "change": manager.getText("changeDigraph"), "ipa": [{"xsampa": "l-_j", "info": None}]}]},
        "м": {"char": "м", "native": "эм", "upper": True, "ipa": [{"xsampa": "m", "info": None}], "variations": []},
        "н": {"char": "н", "native": "эн", "upper": True, "ipa": [{"xsampa": "n", "info": None}], "variations": []},
        "о": {"char": "о", "native": "о", "upper": True, "ipa": [{"xsampa": "o", "info": None}, {"xsampa": "@", "info": manager.getText("whenUnstressed")}], "variations": []},
        "п": {"char": "п", "native": "пэ", "upper": True, "ipa": [{"xsampa": "p", "info": None}], "variations": []},
        "р": {"char": "р", "native": "эр", "upper": True, "ipa": [{"xsampa": "r", "info": None}], "variations": []},
        "с": {"char": "с", "native": "эс", "upper": True, "ipa": [{"xsampa": "s", "info": None}], "variations": []},
        "т": {"char": "т", "native": "тэ", "upper": True, "ipa": [{"xsampa": "t", "info": None}], "variations": []},
        "у": {"char": "у", "native": "у", "upper": True, "ipa": [{"xsampa": "u", "info": None}], "variations": []},
        "ф": {"char": "ф", "native": "эф", "upper": True, "ipa": [{"xsampa": "f", "info": None}], "variations": []},
        "х": {"char": "х", "native": "ха", "upper": True, "ipa": [{"xsampa": "x", "info": None}], "variations": []},
        "ц": {"char": "ц", "native": "цэ", "upper": True, "ipa": [{"xsampa": "t-s", "info": None}], "variations": []},
        "ч": {"char": "ч", "native": "че", "upper": True, "ipa": [{"xsampa": "t-s\\", "info": None}], "variations": []},
        "ш": {"char": "ш", "native": "ша", "upper": True, "ipa": [{"xsampa": "s`", "info": None}], "variations": []},
        "щ": {"char": "щ", "native": "ща", "upper": True, "ipa": [{"xsampa": "s\\-:", "info": None}], "variations": []},
        "ъ": {"char": "ъ", "native": "твёрдый знак", "upper": True, "ipa": [{"xsampa": " ", "info": manager.getText("whenSilent")}], "variations": []},
        "ы": {"char": "ы", "native": "ы", "upper": True, "ipa": [{"xsampa": "1", "info": None}], "variations": []},
        "ь": {"char": "ь", "native": "мягкий знак", "upper": True, "ipa": [{"xsampa": "_j", "info": None}], "variations": []},
        "э": {"char": "э", "native": "э", "upper": True, "ipa": [{"xsampa": "E", "info": None}, {"xsampa": "e", "info": None}], "variations": []},
        "ю": {"char": "ю", "native": "ю", "upper": True, "ipa": [{"xsampa": "j-u", "info": None}, {"xsampa": "_j-u", "info": None}], "variations": []},
        "я": {"char": "я", "native": "я", "upper": True, "ipa": [{"xsampa": "j-a", "info": None}, {"xsampa": "_j-a", "info": None}], "variations": []},
    }

    # [Languages]

    spanish = Window(
        [{"text": character["char"], "command": lambda ch=character: Letter([], ch).load()} for character in spanishCharacters.values()],
        [], manager.getText("whatCharacter")
    )

    russian = Window(
        [{"text": character["char"], "command": lambda ch=character: Letter([], ch).load()} for character in russianCharacters.values()],
        [], manager.getText("whatCharacter")
    )

    # [Main Windows]

    check = Window([
        {"text": manager.getText("spanish"), "command": lambda: spanish.load()},
        {"text": manager.getText("russian"), "command": lambda: russian.load()}
    ], [], manager.getText("whatCheck"))

    language = Window(manager.getLanguages(), [], manager.getText("selectLanguage"))

    settings = Window([
        {"text": manager.getText("settingsLanguage"), "command": lambda: language.load()}
    ], [], manager.getText("whatDo"))

    menu = Window([
        {"text": manager.getText("menuCheck"), "command": lambda: check.load()},
        {"text": manager.getText("menuSettings"), "command": lambda: settings.load()},
        {"text": manager.getText("exit"), "command": lambda: exit()}
    ], [], manager.getText("whatDo"), "", True)

# [Start App]

loadSetup()
menu.load()