def sectionFunctions(name, c):
    path = f"{c.src}/{c.module}.Section{name}.swift"
    lines = c.readFile(path)
    items = []

    for ln in lines:
        if ln.startswith("    static func destroyCore"):
            items.append("destroyCore")
        elif ln.startswith("    static func setupCore"):
            items.append("setupCore")
        elif ln.startswith("    static func setupService"):
            items.append("setupService")

    return items
