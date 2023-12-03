def hasSectionGenerated(entity):
    return len(entity.actions) or len(entity.pipes) or entity.isPresent
