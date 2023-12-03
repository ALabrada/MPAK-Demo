from generation.worldFieldTypeInit import *
from generation.worldFieldTypePS import *

def generateWorldFields(c):
    fileName = f"{c.dir}/templates/world-field"
    lines = c.readFile(fileName)
    fmtInitType = lines[0]
    fmtCVS = lines[1]
    fmtInit = lines[2]
    fmtModel = lines[3]
    fmtNet = lines[4]
    fmtPS = lines[5]
    fmtVar = lines[6]
    fields = []

    for key in c.structure.world.fields:
        values = c.structure.world.fields[key]

        # [TYPE, DEFAULT, cvs] -> CurrentValueSubject
        if "cvs" in values:
            type = values[0]
            default = values[1]
            ln = fmtCVS \
                    .replace("%NAME%", key) \
                    .replace("%TYPE%", type) \
                    .replace("%DEFAULT%", default)
            fields.append(ln)
            
        # [escape, init], [TYPE, escape, init] -> let TYPE
        elif "escape" in values and "init" in values:
            type = worldFieldTypeInit(key, c.structure)
            fmt = fmtInit
            if len(values) == 3:
                fmt = fmtInitType
            ln = fmt \
                    .replace("%NAME%", key) \
                    .replace("%TYPE%", type)
            fields.append(ln)

        # [init], [TYPE, init] -> let TYPE
        elif "init" in values:
            type = worldFieldTypeInit(key, c.structure)
            fmt = fmtInit
            if len(values) == 2:
                fmt = fmtInitType
            ln = fmt \
                    .replace("%NAME%", key) \
                    .replace("%TYPE%", type)
            fields.append(ln)

        # model -> PassthroughSubject<Model>
        elif key == "model":
            fields.append(fmtModel)

        # net -> Net.Publisher
        elif key == "net":
            fields.append(fmtNet)

        # [ps], [TYPE, ps] -> PassthroughSubject
        elif "ps" in values:
            type = worldFieldTypePS(key, c.structure)
            ln = fmtPS \
                    .replace("%NAME%", key) \
                    .replace("%TYPE%", type)
            fields.append(ln)

        # [TYPE, DEFAULT, var] -> var TYPE
        elif "var" in values:
            type = values[0]
            default = values[1]
            ln = fmtVar \
                    .replace("%NAME%", key) \
                    .replace("%TYPE%", type) \
                    .replace("%DEFAULT%", default)
            fields.append(ln)

    c.worldFields = "\n".join(fields)
