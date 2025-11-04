import sys, os, time
from hap.xsampa import IPA

if os.name == "nt":
    def clearScreen(): os.system("cls")
else:
    def clearScreen(): os.system("clear")

def resourcePath(relativePath):
    if hasattr(sys, "_MEIPASS"):
        path = sys._MEIPASS
    else:
        path = os.path.abspath(".")
    return os.path.join(path, relativePath)

def handleInformation(pretext, information, manager):
    if pretext is not None: print(manager.getText(pretext))
    else: print()

    # Iterate and print all texts
    for text in information:
        print(text)

def handleSelection(posttext, options, translate, manager):
    print() # Blank line for spacing

    # Iterate and print all options
    for index, option in enumerate(options, start=1):
        print(f"{index}) {manager.getText(option['text']) if translate or index == len(options) else option['text']}")

    if posttext is not None: print(manager.getText(posttext))
    else: print()

def handleOption(selected, options, manager):
    try:
        selected = int(selected) - 1

        # Check if selected is within range
        if 0 <= selected < len(options):
            # Run lambda function
            options[selected].get("command", lambda: None)()
    except ValueError:
        clearScreen()
        print(manager.getText("invalidOption"))
        input(manager.getText("pressEnter"))

def separateXSAMPA(codes) -> str:
    return "".join(IPA.get(code, "�") for code in codes.split("-"))

def separateInfo(codes, manager):
    return " + ".join(manager.getText(code) for code in codes.split("+"))

def loadIPA(IPACodes, manager) -> str:
    result = []
    for IPACode in IPACodes:
        IPAInfo = f" ({separateInfo(IPACode['info'], manager)})" if IPACode['info'] is not None else ""
        result.append(f"{separateXSAMPA(IPACode['xsampa'])}{IPAInfo}")
    return ", ".join(result)

def loadChar(charInfo, manager, reduced):
    if reduced: print(f"{manager.getText('variationEffect')}: {separateInfo(charInfo['change'], manager)}")
    else:
        char = charInfo['char'].upper() if charInfo['upper'] else ""
        print(f"{manager.getText('charText')}: {char if not reduced else ''}{charInfo['char']}")
        if charInfo['native'] is not None: print(f"{manager.getText('charName')}: {charInfo['native']}")
    print(f"{manager.getText('charIPA')}: {loadIPA(charInfo['ipa'], manager)}")