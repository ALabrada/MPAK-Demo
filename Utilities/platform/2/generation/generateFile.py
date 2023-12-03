def generateFile(c):
    fileName = f"{c.dir}/templates/file"
    fmt = c.readFile(fileName)

    for ln in fmt:
      newLine = ln \
              .replace("%CONTEXT_FIELDS%", c.contextFields) \
              .replace("%CORE%", c.core) \
              .replace("%CORE_SECTION_GENERATED%", c.coreSectionGenerated) \
              .replace("%CORE_SECTION_GENERATED_ACTIONS%", c.coreSectionGeneratedActions) \
              .replace("%CORE_SECTION_GENERATED_PIPES%", c.coreSectionGeneratedPipes) \
              .replace("%CORE_SECTIONS_DESTROY%", c.coreSectionsDestroy) \
              .replace("%CORE_SECTIONS_SETUP%", c.coreSectionsSetup) \
              .replace("%CORE_VM%", c.coreVM) \
              .replace("%CORE_WINDOW%", c.coreWindow) \
              .replace("%IMPORTS%", c.imports) \
              .replace("%MODEL_FIELDS%", c.modelFields) \
              .replace("%SERVICE_CORE%", c.serviceCore) \
              .replace("%SERVICE_SECTION_GENERATED%", c.serviceSectionGenerated) \
              .replace("%SERVICE_SECTION_GENERATED_ACTIONS%", c.serviceSectionGeneratedActions) \
              .replace("%SERVICE_SECTION_GENERATED_PIPES%", c.serviceSectionGeneratedPipes) \
              .replace("%SERVICE_SECTIONS%", c.serviceSections) \
              .replace("%WORLD_CONSTRUCTOR%", c.worldConstructor) \
              .replace("%WORLD_FIELDS%", c.worldFields) \
              .replace("%WORLD_PARAMETERS%", c.worldParameters) \
              .replace("%MODULE%", c.module) \
              .replace("%MODULE_SHORT%", c.shortenName(c.module)) # Замены %MODULE*% должны быть в конце.
      c.file += newLine + "\n"
