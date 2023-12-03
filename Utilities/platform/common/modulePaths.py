def modulePaths(name):
  parts = name.split("/")
  if len(parts) == 2:
    return (name, parts[1])
  else:
    return (name, name)

