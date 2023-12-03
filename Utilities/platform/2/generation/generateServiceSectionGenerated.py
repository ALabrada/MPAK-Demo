def generateServiceSectionGenerated(c):
    fileName = f"{c.dir}/templates/service-section-generated"
    lines = c.readFile(fileName)
    c.serviceSectionGenerated = "\n".join(lines)
