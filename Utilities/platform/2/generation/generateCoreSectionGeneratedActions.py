from generation.sectionGeneratedActionShouldLoad import *

def generateCoreSectionGeneratedActions(c):
    fileName = f"{c.dir}/templates/core-section-generated-action"
    lines = c.readFile(fileName)

    for key in c.structure.core.actions:
        value = c.structure.core.actions[key]

        # Шаблонные действия.
        if value == "":
            # shouldLoad*.
            shouldLoad = "shouldLoad"
            if key.startswith(shouldLoad):
                c.coreSectionGeneratedActions += sectionGeneratedActionShouldLoad(key, "core", c)
                continue

            continue
        

        output = ""
        for fmt in lines:
            ln = fmt \
                    .replace("%SHOULD%", key) \
                    .replace("%SINK%", value)
            output += ln + "\n"

        c.coreSectionGeneratedActions += output
