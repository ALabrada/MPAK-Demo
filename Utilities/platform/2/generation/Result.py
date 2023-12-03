class Result:
    def __init__(self, dir, path, module, readFile, shortenName, src, structure):
        self.dir = dir
        self.path = path
        self.module = module
        self.readFile = readFile
        self.shortenName = shortenName
        self.src = src
        self.structure = structure

        self.contextFields = ""
        self.core = ""
        self.coreSectionGenerated = ""
        self.coreSectionGeneratedActions = ""
        self.coreSectionGeneratedPipes = ""
        self.coreSectionsDestroy = ""
        self.coreSectionsSetup = ""
        self.coreVM = ""
        self.coreWindow = ""
        self.file = ""
        self.imports = ""
        self.modelFields = ""
        self.serviceCore = ""
        self.serviceSectionGenerated = ""
        self.serviceSectionGeneratedActions = ""
        self.serviceSectionGeneratedPipes = ""
        self.serviceSections = ""
        self.worldFields = ""
        self.worldParameters = ""
