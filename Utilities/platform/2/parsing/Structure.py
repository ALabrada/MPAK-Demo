from parsing.CoreService import *
from parsing.ModelWorld import *

class Structure:
    def __init__(self):
        self.core = CoreService()
        self.model = ModelWorld()
        self.service = CoreService()
        self.world = ModelWorld()
