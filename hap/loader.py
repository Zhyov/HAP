import json, os

def loadAlphabetsManifest():
    base = os.path.join(os.path.dirname(__file__), "data", "alphabets")
    with open(os.path.join(base, "manifest.json"), encoding="utf-8") as f:
        return json.load(f)

def loadCharacters(filename):
    base = os.path.join(os.path.dirname(__file__), "data", "alphabets")
    with open(os.path.join(base, filename), encoding="utf-8") as f:
        return json.load(f)