def readKeyValue(line):
    parts = line.split(": ")
    # Ключ со значением.
    if len(parts) == 2:
        return (parts[0], parts[1])

    # Не является ключом со значением.
    return None
