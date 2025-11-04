import json, os
from hap.utils import resourcePath

def loadAlphabetsManifest():
    base = resourcePath(os.path.join("hap", "data", "alphabets"))
    with open(os.path.join(base, "manifest.json"), encoding="utf-8") as f:
        return json.load(f)

def loadCharacters(filename):
    base = resourcePath(os.path.join("hap", "data", "alphabets"))
    with open(os.path.join(base, filename), encoding="utf-8") as f:
        return json.load(f)