def valueArray(value):
    # Удостоверяем наличие скобок.
    if not (
        value.startswith("[") and
        value.endswith("]")
       ):
        return None

    # Исключаем скобки.
    noBrackets = value[1:-1]
    parts = noBrackets.split(", ")
    return parts
