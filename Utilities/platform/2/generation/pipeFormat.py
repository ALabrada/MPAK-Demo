def pipeFormat(fmtExRecent, fmtRecent, fmtSet, fmtToggle, fmtToggleNil, name, entity):
    props = entity.pipes[name]
    if "recent" and "ex" in props:
        return fmtExRecent
    elif "recent" in props:
        return fmtRecent
    elif "set" in props:
        return fmtSet
    elif "toggle" in props:
        return fmtToggle
    elif "toggleNil" in props:
        return fmtToggleNil

    return "НИНАЮ"
