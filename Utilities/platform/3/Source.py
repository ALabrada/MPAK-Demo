from readKeyValue import *

class Source:
    def __init__(self):
        self.name = ""

    def parseLine(self, line):
        kv = readKeyValue(line)
        # Игнорируем всё, что не является ключом со значением.
        if kv is None:
            return

        self.name = kv[1]
