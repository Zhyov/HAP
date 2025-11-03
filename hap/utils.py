import os
from hap.xsampa import IPA

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
    return "".join(IPA.get(code, "?") for code in codes.split("-"))

def separateInfo(codes, manager):
    return " + ".join(manager.getText(code) for code in codes.split("+"))

def loadIPA(IPACodes, manager):
    result = []
    for IPACode in IPACodes:
        IPAInfo = f" ({separateInfo(IPACode['info'], manager)})" if IPACode['info'] is not None else ""
        result.append(f"{separateXSAMPA(IPACode['xsampa'])}{IPAInfo}")
    return ", ".join(result)

def loadChar(charInfo, manager, reduced: bool = False):
    if reduced: print(f"{manager.getText('variationEffect')}: {charInfo['change']}")
    else:
        char = charInfo['char'].upper() if charInfo['upper'] else ""
        print(f"{manager.getText('charText')}: {char if not reduced else ''}{charInfo['char']}")
        if charInfo['native'] is not None: print(f"{manager.getText('charName')}: {charInfo['native']}")
    print(f"{manager.getText('charIPA')}: {loadIPA(charInfo['ipa'], manager)}")