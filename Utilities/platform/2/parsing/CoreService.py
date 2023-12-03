from parsing.readKeyValue import *
from parsing.valueArray import *

class CoreService:
    def __init__(self):
        self.actions = {}
        self.isPresent = False
        self.pipes = {}

    def parseAction(self, line):
        kv = readKeyValue(line)

        # В действии всегда должен быть хотя бы ключ.
        if kv is None:
            return

        # Лишь ключ.
        if kv[1] is None:
            self.actions[kv[0]] = ""
            return

        # Ключ и значение.
        self.actions[kv[0]] = kv[1]

    def parsePipe(self, line):
        kv = readKeyValue(line)
        # В канале всегда должны быть и ключ, и значение.
        if (
            kv is None or
            kv[1] is None
           ):
            return

        values = valueArray(kv[1])
        # В канале каждое значение должно быть массивом.
        if values is None:
            return

        self.pipes[kv[0]] = values
