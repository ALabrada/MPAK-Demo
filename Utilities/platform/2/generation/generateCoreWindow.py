from generation.sectionNames import *

def generateCoreWindow(c):
    fileName = f"{c.dir}/templates/core-window"
    lines = c.readFile(fileName)
    fmtV = lines[0]
    fmtW = lines[1]
    sections = sectionNames(c)
    if "UI" in sections:
        c.coreVM = fmtV
        c.coreWindow = fmtW
