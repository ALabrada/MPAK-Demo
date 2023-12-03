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

        # featureToggle.
        if mode.isFeatureToggle:
            structure.featureToggle.parseLine(ln)
