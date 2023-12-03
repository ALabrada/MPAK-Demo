def readKeyValue(line):
    parts = line.split(": ")
    # Ключ со значением.
    if len(parts) == 2:
        return (parts[0], parts[1])

    # Ключ без значения.
    if (
        line.endswith(":") == False and
        len(parts) == 1
       ):
        return (parts[0], None)

    # Не является ключом со значением.
    return None
