def sectionGeneratedActionShouldLoad(key, sub, c):
    lines = c.readFile(f"{c.dir}/templates/section-generated-action-shouldLoad")
    name = key[len("shouldLoad"):]
    request = name[0].lower() + name[1:]
    output = ""

    for fmt in lines:
        ln = fmt \
                .replace("%NAME%", name) \
                .replace("%REQUEST%", request) \
                .replace("%SUB%", sub)
        output += ln + "\n"

    return output
