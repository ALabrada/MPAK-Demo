from generation.sectionFunctions import *
from generation.sectionNames import *

def generateCoreSectionsDestroy(c):
    fileName = f"{c.dir}/templates/core-section"
    fmt = c.readFile(fileName)[0]
    items = []

    sections = sectionNames(c)
    for name in sections:
        # Пропускаем секции, не относящиеся к удалению ядра.
        funcs = sectionFunctions(name, c)
        if "destroyCore" not in funcs:
            continue

        ln = fmt.replace("%NAME%", name)
        items.append(ln)

    c.coreSectionsDestroy = "\n".join(items)
