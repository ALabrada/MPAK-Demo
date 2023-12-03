def readFile(fileName):
    lines = []
    with open(fileName) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines
