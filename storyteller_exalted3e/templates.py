from django.conf import settings
from storyteller.base import Template

_EXIGENT_CHARMS = ["Offensive", "Defensive", "Social", "Mobility and Travel"]


class _Ex3Template(Template):
    power_stat = "Essence"
    native_charms = None
    game = "Exalted 3e"
    charm_categories = []

    def calculate_personal_motes(self, target: "DefaultCharacter"):
        return 0

    def calculate_peripheral_motes(self, target: "DefaultCharacter"):
        return 0


class Mortal(_Ex3Template):
    fields = []


class Solar(_Ex3Template):
    fields = ["Caste"]
    field_defaults = {"Caste": "Dawn"}
    field_choices = {"Caste": ["Dawn", "Zenith", "Twilight", "Night", "Eclipse"]}
    native_charms = "Solar"
    charm_categories = settings.STORYTELLER_ABILITIES


class Lunar(_Ex3Template):
    fields = ["Caste", "Spirit Shape"]
    field_defaults = {"Caste": "Casteless"}
    field_choices = {"Caste": ["Full Moon", "Changing Moon", "No Moon", "Casteless"]}
    native_charms = "Lunar"
    charm_categories = settings.STORYTELLER_ATTRIBUTES + ["Universal"]


class DragonBlooded(_Ex3Template):
    name = "Dragon-Blooded"
    fields = ["Aspect"]
    field_defaults = {"Aspect": "Air"}
    field_choices = {"Aspect": ["Air", "Earth", "Fire", "Water", "Wood"]}
    native_charms = "Dragon-Blooded"
    charm_categories = settings.STORYTELLER_ABILITIES


class Sidereal(_Ex3Template):
    fields = ["Caste"]
    field_defaults = {"Caste": "Journeys"}
    field_choices = {"Caste": ["Journeys", "Battles", "Secrets", "Endings", "Serenity"]}
    native_charms = "Sidereal"
    charm_categories = settings.STORYTELLER_ABILITIES + [
        "Journeys",
        "Battles",
        "Secrets",
        "Endings",
        "Serenity",
    ]


class Abyssal(Solar):
    fields = ["Caste"]
    field_defaults = {"Caste": "Dusk"}
    field_choices = {"Caste": ["Dusk", "Midnight", "Daybreak", "Day", "Moonshadow"]}
    native_charms = "Abyssal"


class Infernal(Solar):
    fields = ["Caste"]
    field_defaults = {"Caste": "Azimuth"}
    field_choices = {"Caste": ["Azimuth", "Ascendant", "Horizon", "Nadir", "Penumbra"]}
    native_charms = "Infernal"


class Alchemical(_Ex3Template):
    fields = ["Caste"]
    field_defaults = {"Caste": "Orichalcum"}
    field_choices = {
        "Caste": [
            "Orichalcum",
            "Moonsilver",
            "Starmetal",
            "Jade",
            "Soulsteel",
            "Adamant",
        ]
    }
    native_charms = "Alchemical"
    charm_categories = settings.STORYTELLER_ATTRIBUTES


class Liminal(_Ex3Template):
    fields = ["Aspect"]
    field_defaults = {"Aspect": "Blood"}
    field_choices = {"Aspect": ["Blood", "Breath", "Flesh", "Marrow", "Soil"]}
    native_charms = "Liminal"
    charm_categories = settings.STORYTELLER_ATTRIBUTES


class Getimian(_Ex3Template):
    fields = ["Caste"]
    field_defaults = {"Caste": "Spring"}
    field_choices = {"Caste": ["Spring", "Summer", "Autumn", "Winter"]}
    native_charms = "Getimian"
    charm_categories = settings.STORYTELLER_ATTRIBUTES


class Exigent(_Ex3Template):
    fields = ["Tier", "Type", "Patron"]
    field_defaults = {"Tier": "Terrestrial", "Type": "Essence"}
    field_choices = {
        "Tier": ["Terrestrial", "Celestial"],
        "Type": ["Essence", "Attribute", "Ability"],
    }
    native_charms = "Exigent"
    charm_categories = (
        settings.STORYTELLER_ATTRIBUTES
        + settings.STORYTELLER_ABILITIES
        + _EXIGENT_CHARMS
        + ["Mysticism", "Universal", "Essence"]
    )


class Architect(_Ex3Template):
    fields = ["City"]
    native_charms = "Architect"
    charm_categories = settings.STORYTELLER_ATTRIBUTES


class DreamSouled(_Ex3Template):
    name = "Dream-Souled"
    native_charms = "Dream-Souled"
    charm_categories = ["Illusion and Transformation"] + _EXIGENT_CHARMS


class Sovereign(_Ex3Template):
    native_charms = "Sovereign"
    charm_categories = settings.STORYTELLER_ABILITIES


class Hearteater(_Ex3Template):
    native_charms = "Hearteater"
    charm_categories = ["Pawn"] + _EXIGENT_CHARMS + ["Mysticism"]


class Umbral(_Ex3Template):
    native_charms = "Umbral"
    charm_categories = ["Penumbra", "Darkness"] + _EXIGENT_CHARMS + ["Mysticism"]


class _Spirit(_Ex3Template):
    native_charms = "Spirit"
    charm_categories = ["Universal"] + _EXIGENT_CHARMS + ["Essence", "Mysticism"]


class God(_Spirit):
    name = "God"
    fields = ["Purview"]


class Elemental(_Spirit):
    name = "Elemental"
    fields = ["Element"]
    field_choices = {"Element": ["Air", "Earth", "Fire", "Water"]}


class Demon(_Spirit):
    name = "Demon"
    fields = ["Type", "Oversoul"]
    field_choices = {"Type": ["First Circle", "Second Circle", "Third Circle"]}
    field_Defaults = {"Type": "First Circle"}


ALL_TEMPLATES = [
    Mortal,
    Solar,
    Lunar,
    DragonBlooded,
    Sidereal,
    Abyssal,
    Infernal,
    Alchemical,
    Liminal,
    Getimian,
    Exigent,
    Architect,
    DreamSouled,
    Sovereign,
    Hearteater,
    Umbral,
    God,
    Elemental,
    Demon,
]
