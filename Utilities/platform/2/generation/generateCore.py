def generateCore(c):
    fileName = f"{c.dir}/templates/core"
    lines = c.readFile(fileName)
    c.core = "\n".join(lines)

    fileName = f"{c.dir}/templates/service-core"
    c.serviceCore = c.readFile(fileName)[0]
