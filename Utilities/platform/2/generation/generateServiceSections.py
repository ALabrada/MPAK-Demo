from generation.hasSectionGenerated import *
from generation.sectionFunctions import *
from generation.sectionNames import *

def generateServiceSections(c):
    fileName = f"{c.dir}/templates/service-section"
    lines = c.readFile(fileName)
    fmtService = lines[0]
    fmtPlatform = lines[1]
    items = []

    sections = sectionNames(c)
    for name in sections:
        # Пропускаем секции, не относящиеся к сервису.
        funcs = sectionFunctions(name, c)
        if "setupService" not in funcs:
            continue

        ln = fmtService.replace("%NAME%", name)
        items.append(ln)

    # Генерированная секция.
    # Должна быть добавлена последней.
    if hasSectionGenerated(c.structure.service):
        items.append(fmtPlatform)

    c.serviceSections= "\n".join(items)
