from generation.isPipeRecent import *

def fieldFormat(fmtPlain, fmtRecent, name, structure):
    fmt = fmtPlain
    if (
        isPipeRecent(name, structure.core) or
        isPipeRecent(name, structure.service)
      ):
        fmt = fmtRecent
    return fmt
