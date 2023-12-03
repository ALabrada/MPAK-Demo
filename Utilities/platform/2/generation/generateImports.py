def generateImports(c):
    fileName = f"{c.src}/../{c.module}.podspec"
    # Для сборного модуля используем путь к корневому podspec.
    if c.path != c.module:
      parent = c.path.split("/")[0]
      fileName = fileName.replace(f"{c.module}/src/../{c.module}", parent)
    lines = c.readFile(fileName)
    items = ["Combine"]

    prefix = "s.dependency '"
    for ln in lines:
        if ln.startswith(prefix):
            name = ln[len(prefix):-1]
            items.append(name)

    c.imports = "import " + "\nimport ".join(sorted(items))
