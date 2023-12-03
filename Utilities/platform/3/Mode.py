class Mode:
    def __init__(self):
        self.reset()

    def parseLine(self, line):
        if line.startswith("src:"):
            self.reset()
            self.isSource  = True
        elif line.startswith("replace:"):
            self.reset()
            self.isReplacement = True

    def reset(self):
        self.isSource = False
        self.isReplacement = False
