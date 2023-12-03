from parsing.readKeyValue import *
from parsing.valueArray import *

class ModelWorld:
    def __init__(self):
        self.fields = {}

    def parseLine(self, line):
        kv = readKeyValue(line)
        # В модели/мире всегда должен быть хотя бы ключ.
        if kv is None:
            return

        # Лишь ключ.
        if kv[1] is None:
            self.fields[kv[0]] = []
            return

        values = valueArray(kv[1])
        # В модели/мире указанное значение должно быть массивом.
        if values is None:
            return

        self.fields[kv[0]] = values
