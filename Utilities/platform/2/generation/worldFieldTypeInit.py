from generation.isToggle import *
    
_keywords = { "init", "var", "escape" }

def worldFieldTypeInit(key, structure):
    values = structure.world.fields[key]
    values = [v for v in values if v not in _keywords]
    if len(values) == 1:
        return values[0]
    if isToggle(key, structure):
        return "Void"
    return structure.model.fields[key][0]
