def shortenName(text):
    capitals = [l for l in text if l.isupper()]
    # Нет заглавных.
    if len(capitals) == 0:
        return text

    capId = 0
    # Первая - заглавная.
    if text[0].isupper():
        capId = 1

    # Заглавная лишь первая.
    if (
        capId == 1 and
        len(capitals) == 1
       ):
        return text

    # Убираем первое заглавное слово.
    if capId == 1:
        capitals = capitals[1:]
    # Есть ещё заглавные.
    firstCap = text.find(capitals[0])
    return text[:firstCap] + "".join(capitals)
