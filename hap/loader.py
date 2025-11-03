import json, os

def loadCharacters(filename):
    base = os.path.join(os.path.dirname(__file__), "data", "lang")
    with open(os.path.join(base, filename), encoding="utf-8") as f:
        return json.load(f)