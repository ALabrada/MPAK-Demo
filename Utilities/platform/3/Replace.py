from readKeyValue import *

class Replace:
    def __init__(self):
        self.items = { }

    def parseLine(self, line):
        kv = readKeyValue(line)
        # Игнорируем всё, что не является ключом со значением.
        if kv is None:
            return
        self.items[kv[0]] = kv[1]
