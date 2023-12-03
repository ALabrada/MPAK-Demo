from Mode import *

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

        # replace.
        if mode.isReplacement:
            structure.replace.parseLine(ln)
        # src.
        elif mode.isSource:
            structure.src.parseLine(ln)
