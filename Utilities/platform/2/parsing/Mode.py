class Mode:
    def __init__(self):
        self.reset()

    def parseLine(self, line):
        if line.startswith("model:"):
            self.reset()
            self.isModel = True
        elif line.startswith("core:"):
            self.reset()
            self.isCore = True
        elif line.startswith("service:"):
            self.reset()
            self.isService = True
        elif line.startswith("world:"):
            self.reset()
            self.isWorld = True
        elif line.startswith("  actions:"):
            self.isAction = True
            self.isPipe = False
        elif line.startswith("  pipes:"):
            self.isAction = False
            self.isPipe = True

    def reset(self):
        self.isAction = False
        self.isCore = False
        self.isModel = False
        self.isPipe = False
        self.isService = False
        self.isWorld = False
