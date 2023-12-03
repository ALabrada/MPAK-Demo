def isToggle(name, structure):
    # Проверяем наличие `toggle` в свойствах канала ядра.
    if name in structure.core.pipes:
        props = structure.core.pipes[name]
        if "toggle" in props:
            return True

    # Проверяем наличие `toggle` в свойствах канала сервиса.
    if name in structure.service.pipes:
        props = structure.service.pipes[name]
        if "toggle" in props:
            return True

    return False
