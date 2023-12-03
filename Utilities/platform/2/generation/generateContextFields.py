from generation.fieldFormat import *

def generateContextFields(c):
    fileName = f"{c.dir}/templates/context-field"
    lines = c.readFile(fileName)
    fmtPlain = lines[0]
    fmtRecent = lines[1]
    fields = []

    for key in c.structure.model.fields:
        values = c.structure.model.fields[key]
        fmt = fieldFormat(fmtPlain, fmtRecent, key, c.structure)
        ln = fmt \
                .replace("%NAME%", key) \
                .replace("%TYPE%", values[0])
        fields.append(ln)

    c.contextFields = "\n".join(fields)
