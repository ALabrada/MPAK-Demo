from generation.isNotKeyword import *

def pipeSource(name, entity):
    props = entity.pipes[name]
    if "vm" in props:
        return "core.vm." + name
    elif "$vm" in props:
        return "core.vm.$" + name
    else:
        # Если это что-то неизвестное заранее, то ищем строку,
        # отличную от известных ключевых слов для инструкции pipe.
        default = "world"
        src = next(filter(isNotKeyword, props), default)
        # Прямое обращение к VM.
        if src.startswith("vm."):
            src = "core." + src
        # Значение по умолчанию.
        elif src == default:
            return default + "." + name
        return src
