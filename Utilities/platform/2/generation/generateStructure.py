from generation.generateContextFields import *
from generation.generateCore import *
from generation.generateCoreSectionGenerated import *
from generation.generateCoreSectionGeneratedActions import *
from generation.generateCoreSectionsDestroy import *
from generation.generateCoreSectionsSetup import *
from generation.generateCoreWindow import *
from generation.generateFile import *
from generation.generateImports import *
from generation.generateModelFields import *
from generation.generateServiceSectionGenerated import *
from generation.generateServiceSectionGeneratedActions import *
from generation.generateServiceSections import *
from generation.generateWorldConstructor import *
from generation.generateWorldFields import *
from generation.generateWorldParameters import *
from generation.hasSectionGenerated import *
from generation.sectionGeneratedPipes import *

def generateStructure(c):
    generateContextFields(c)
    generateImports(c)
    generateModelFields(c)
    # Генерируем ядро лишь при наличии инструкций в YML.
    if hasSectionGenerated(c.structure.core):
        generateCore(c)
        generateCoreSectionsDestroy(c)
        generateCoreSectionsSetup(c)
        generateCoreWindow(c)
        generateCoreSectionGenerated(c)
        generateCoreSectionGeneratedActions(c)
        c.coreSectionGeneratedPipes = sectionGeneratedPipes(c.structure.core, "&core.subscriptions", c)
    generateServiceSections(c)
    # Генерируем секцию сервиса лишь при наличии инструкций в YML.
    if hasSectionGenerated(c.structure.service):
        generateServiceSectionGenerated(c)
        generateServiceSectionGeneratedActions(c)
        c.serviceSectionGeneratedPipes = sectionGeneratedPipes(c.structure.service, "nil", c)
    generateWorldConstructor(c)
    generateWorldFields(c)
    generateWorldParameters(c)
    # Файл обязательно генерировать последним: зависит от остальных.
    generateFile(c)
