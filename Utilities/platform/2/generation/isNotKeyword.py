def isNotKeyword(str):
    keywords = [
        "ex",
        "recent",
        "set",
        "toggle",
        "toggleNil",
        "vm",
        "$vm"
    ]
    return str not in keywords
