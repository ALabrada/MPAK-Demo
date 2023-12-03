from generation.shortenName import *
from generation.pipeFormat import *
from generation.pipeSource import *

def sectionGeneratedPipes(entity, sub, c):
    fmtExRecent = c.readFile(f"{c.dir}/templates/section-generated-pipe-ex-recent")
    fmtRecent = c.readFile(f"{c.dir}/templates/section-generated-pipe-recent")
    fmtSet = c.readFile(f"{c.dir}/templates/section-generated-pipe-set")
    fmtToggle = c.readFile(f"{c.dir}/templates/section-generated-pipe-toggle")
    fmtToggleNil = c.readFile(f"{c.dir}/templates/section-generated-pipe-toggleNil")
    output = ""

    for key in entity.pipes:
        values = entity.pipes[key]

        # EX_NAME.
        firstLetter = key[:1].capitalize()
        exName = f"""ex{firstLetter}{key[1:]}"""

        # PIPE.
        pipe = "pipeValue"
        if "toggle" in values:
            pipe = "pipe"

        # SHORT_SRC.
        shortSrc = shortenName(key)

        # SRC.
        src = pipeSource(key, entity)

        fmtPipe = pipeFormat(fmtExRecent, fmtRecent, fmtSet, fmtToggle, fmtToggleNil, key, entity)
        for fmt in fmtPipe:
            ln = fmt \
                    .replace("%EX_NAME%", exName) \
                    .replace("%NAME%", key) \
                    .replace("%PIPE%", pipe) \
                    .replace("%SHORT_SRC%", shortSrc) \
                    .replace("%SRC%", src) \
                    .replace("%SUB%", sub)
            output += ln + "\n"

    return output
