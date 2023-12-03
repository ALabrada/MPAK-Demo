from generation.hasSectionGenerated import *
from generation.sectionFunctions import *
from generation.sectionNames import *

def generateCoreSectionsSetup(c):
    fileName = f"{c.dir}/templates/core-section"
    lines = c.readFile(fileName)
    fmtCore = lines[1]
    fmtPlatform = lines[2]
    items = []

    sections = sectionNames(c)
    for name in sections:
        # Пропускаем секции, не относящиеся к установке ядра.
        funcs = sectionFunctions(name, c)
        if "setupCore" not in funcs:
            continue

        ln = fmtCore.replace("%NAME%", name)
        items.append(ln)

    # Генерированная секция.
    # Должна быть добавлена последней.
    if hasSectionGenerated(c.structure.core):
        items.append(fmtPlatform)

    c.coreSectionsSetup = "\n".join(items)
