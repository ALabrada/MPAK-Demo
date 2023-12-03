from parsing.CoreService import *
from parsing.Mode import *
from parsing.ModelWorld import *

def parseLines(lines, structure):
    mode = Mode()
    for line in lines:
        # Определяем режим строки.
        mode.parseLine(line)
        ln = line.strip()

        # Игнорируем пустую строку.
        if len(ln) == 0:
            continue

        # Игнорируем комментарий.
        if ln.startswith("#"):
            continue

        # model.
        if mode.isModel:
            structure.model.parseLine(ln)

        # core.
        elif mode.isCore:
            structure.core.isPresent = True
            if mode.isAction:
              structure.core.parseAction(ln)
            elif mode.isPipe:
              structure.core.parsePipe(ln)

        # service.
        elif mode.isService:
            structure.service.isPresent = True
            if mode.isAction:
              structure.service.parseAction(ln)
            elif mode.isPipe:
              structure.service.parsePipe(ln)

        # world.
        elif mode.isWorld:
            structure.world.parseLine(ln)
