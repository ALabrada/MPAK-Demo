def generateWorldConstructor(c):
    fileName = f"{c.dir}/templates/world-constructor"
    fmt = c.readFile(fileName)[0]

    items = []

    for key in c.structure.world.fields:
        values = c.structure.world.fields[key]

        if (
            "init" in values or
            key == "model" or
            key == "net"
           ):
            ln = fmt.replace("%NAME%", key)
            items.append(ln)

    c.worldConstructor = "\n".join(items)
