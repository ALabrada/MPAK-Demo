from generation.worldFieldTypeInit import *

def generateWorldParameters(c):
    fileName = f"{c.dir}/templates/world-parameter"
    lines = c.readFile(fileName)
    fmtInitType = lines[0]
    fmtEscInitType = lines[1]
    fmtInit = lines[2]
    fmtModel = lines[3]
    fmtNet = lines[4]

    params = []

    for key in c.structure.world.fields:
        values = c.structure.world.fields[key]

        if "init" in values:
            type = worldFieldTypeInit(key, c.structure)
            fmt = fmtInit
            if "escape" in values:
                fmt = fmtEscInitType
            elif len(values) > 1:
                fmt = fmtInitType
            ln = fmt \
                    .replace("%NAME%", key) \
                    .replace("%TYPE%", type)
            params.append(ln)

        elif key == "model":
            params.append(fmtModel)

        elif key == "net":
            params.append(fmtNet)

    c.worldParameters = ",\n".join(params)
