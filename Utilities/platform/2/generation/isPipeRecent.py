def isPipeRecent(name, entity):
    if name in entity.pipes:
        props = entity.pipes[name]
        return "recent" in props
    return False
