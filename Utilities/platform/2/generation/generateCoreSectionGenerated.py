def generateCoreSectionGenerated(c):
    fileName = f"{c.dir}/templates/core-section-generated"
    lines = c.readFile(fileName)
    c.coreSectionGenerated = "\n".join(lines)
