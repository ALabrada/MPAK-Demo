def generateStructure(structure):
    output = f"""// ВНИМАНИЕ Сгенерировано автоматом из файла {structure.src.name}.yml
// ВНИМАНИЕ Не менять руками!
"""
    output += structure.orig
    for key in structure.replace.items:
        value = structure.replace.items[key]
        output = output.replace(key, value)
    return output
