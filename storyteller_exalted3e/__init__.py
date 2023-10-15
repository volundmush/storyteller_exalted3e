def init(settings, plugins):
    settings.STORYTELLER_TEMPLATE_MODULES.append("storyteller.exalted3e.templates")

    settings.STORYTELLER_ADVANTAGES = ["Essence", "Willpower"]

    settings.STORYTELLER_ATTRIBUTES = [
        "Strength",
        "Dexterity",
        "Stamina",
        "Charisma",
        "Manipulation",
        "Appearance",
        "Intelligence",
        "Wits",
        "Perception",
    ]

    settings.STORYTELLER_ABILITIES = [
        "Archery",
        "Athletics",
        "Awareness",
        "Brawl",
        "Bureaucracy",
        "Craft",
        "Dodge",
        "Integrity",
        "Investigation",
        "Larceny",
        "Linguistics",
        "Lore",
        "Martial Arts",
        "Medicine",
        "Melee",
        "Occult",
        "Performance",
        "Presence",
        "Resistance",
        "Ride",
        "Sail",
        "Socialize",
        "Stealth",
        "Survival",
        "Thrown",
        "War",
    ]

    settings.STORYTELLER_SKILLS = settings.STORYTELLER_ABILITIES

    settings.BASE_CHARACTER_TYPECLASS = "storyteller_exalted3e.characters.Ex3Character"

    settings.STORYTELLER_ROOT = "storyteller_exalted3e.stats.Root"

    settings.STORYTELLER_ATTRIBUTE_OPTIONS = ("set", "tag", "untag")
