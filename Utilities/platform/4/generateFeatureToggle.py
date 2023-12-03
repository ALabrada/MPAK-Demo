from pathlib import Path

def generateFeatureToggle(s):
    # Пропускаем генерацию FeatureToggle, если не указана ссылка ivcsdbg
    if s.featureToggle.link is None:
        return

    # Создаём директории модуля.
    dirs = f"{s.moduleDir}/{s.module}FeatureToggle/src"
    Path(dirs).mkdir(parents=True, exist_ok=True)

    # Создаём YML для генератора-3.
    content = f"""version: 3

# ВНИМАНИЕ Сгенерировано автоматом из файла {s.module}.yml
# ВНИМАНИЕ Не менять руками!

src: ChatsFeatureToggle
replace:
  ChatsFeatureToggle: {s.module}FeatureToggle
  ChatsFTCtrl: {s.module}FTCtrl
  chats: {s.featureToggle.link}
"""

    # Сохраняем YML.
    fileName = f"{s.moduleDir}/{s.module}FeatureToggle/{s.module}FeatureToggle.yml"
    with open(fileName, "w") as file:
        file.write(content)
