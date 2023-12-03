from generation.sectionGeneratedActionShouldLoad import *

def generateServiceSectionGeneratedActions(c):
    base = f"{c.dir}/templates/service-section-generated-action"
    fmtCommon = c.readFile(base)
    fmtInstant = c.readFile(f"{base}-instant")
    fmtInstantModel = c.readFile(f"{base}-instant-model")
    fmtInstantShouldResetCore = c.readFile(f"{base}-instant-shouldResetCore")
    fmtModel = c.readFile(f"{base}-model")
    fmtShouldResetCore = c.readFile(f"{base}-shouldResetCore")

    for key in c.structure.service.actions:
        value = c.structure.service.actions[key]

        # Шаблонные действия.
        if value == "":            
            # instant model.
            if key == "🚀model":
                c.serviceSectionGeneratedActions += "\n".join(fmtInstantModel) + "\n"
                continue
            
            # model.
            if key == "model":
                c.serviceSectionGeneratedActions += "\n".join(fmtModel) + "\n"
                continue
        
            # shouldLoad*.
            shouldLoad = "shouldLoad"
            if key.startswith(shouldLoad):
                c.serviceSectionGeneratedActions += sectionGeneratedActionShouldLoad(key, "service", c)
                continue
            
            # instant shouldResetCore.
            if key == "🚀shouldResetCore":
                c.serviceSectionGeneratedActions += "\n".join(fmtInstantShouldResetCore) + "\n"
                continue
            
            # shouldResetCore.
            if key == "shouldResetCore":
                c.serviceSectionGeneratedActions += "\n".join(fmtShouldResetCore) + "\n"
                continue

            continue

        output = ""

        action = key
        template = fmtCommon
        # Действие без receive(on:)
        if action.startswith("🚀"):
            action = action[1:]
            template = fmtInstant

        for fmt in template:
            ln = fmt \
                    .replace("%SHOULD%", action) \
                    .replace("%SINK%", value)
            output += ln + "\n"

        c.serviceSectionGeneratedActions += output
