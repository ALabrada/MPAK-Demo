from generation.isToggle import *

def worldFieldTypePS(key, structure):
    values = structure.world.fields[key]
    if len(values) == 2:
        return values[0]
    if isToggle(key, structure):
        return "Void"
    return structure.model.fields[key][0]
