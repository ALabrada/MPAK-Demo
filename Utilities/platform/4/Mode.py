class Mode:
    def __init__(self):
        self.reset()

    def parseLine(self, line):
        if line.startswith("featureToggle:"):
            self.reset()
            self.isFeatureToggle = True

    def reset(self):
        self.isFeatureToggle = False
