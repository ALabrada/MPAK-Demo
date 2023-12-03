import os

def readModuleSrc(dir, readFile):
    fileNames = os.listdir(dir)
    contents = []

    for fileName in sorted(fileNames):
        path = dir + "/" + fileName
        lines = readFile(path)
        contents.extend(lines)

    return "\n".join(contents)
