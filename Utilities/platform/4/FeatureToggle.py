from readKeyValue import *

class FeatureToggle:
    def __init__(self):
        self.link = None

    def parseLine(self, line):
        kv = readKeyValue(line)
        # Игнорируем всё, что не является ключом со значением.
        if kv is None:
            return

        self.link = kv[1]
