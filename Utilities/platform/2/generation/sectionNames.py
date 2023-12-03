import os

def sectionNames(c):
    prefix = "Section"
    ending = ".swift"
    fileNames = os.listdir(c.src)
    items = []

    for fileName in sorted(fileNames):
        # Пропускаем файлы, не являющиеся секциями.
        id = fileName.find(prefix)
        if id == -1:
            continue

        # Вычленяем имя секции из имени файла.
        name = fileName[id + len(prefix):-len(ending)]
        items.append(name)

    return items
