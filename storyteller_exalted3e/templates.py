from storyteller.base import Template
from storyteller.utils import get_story

_EXIGENT_CHARMS = ["Offensive", "Defensive", "Social", "Mobility and Travel"]


class _Ex3Template(Template):
    power_stat = "Essence"
    native_charms = None
    charm_categories = []
    advantages = ["Willpower", "Essence"]
    sheet_footer = "Exalted Third Edition"


class Mortal(_Ex3Template):
    fields = []
    pools = ["Willpower"]


class _Ex3Exalt(_Ex3Template):
    pools = ["Personal", "Peripheral", "Willpower", "Limit"]


class Solar(_Ex3Exalt):
    fields = ["Caste"]
    field_defaults = {"Caste": "Dawn"}
    field_choices = {"Caste": ["Dawn", "Zenith", "Twilight", "Night", "Eclipse"]}
    native_charms = "Solar"
    ability_tier = "Normal: |w0|n, Favored: |w1|n, Caste: |w2|n, Supernal: |w3|n"
    ability_options = ["tier"]
    color_overrides = {"border": "Y", "title": "y", "slash": "r"}
    sheet_footer = f"Solars: The Lawgivers of Creation"

    @property
    def charm_categories(self):
        return self.game.abilities + ["Eclipse"]

    def calculate_pool_max_personal(self, target: "DefaultCharacter"):
        ess = self.get_advantage(target, "Essence")
        return 10 + (ess * 3)

    def calculate_pool_max_peripheral(self, target: "DefaultCharacter"):
        ess = self.get_advantage(target, "Essence")
        return 26 + (ess * 7)


class Lunar(_Ex3Exalt):
    fields = ["Caste", "Spirit Shape"]
    field_defaults = {"Caste": "Casteless"}
    field_choices = {"Caste": ["Full Moon", "Changing Moon", "No Moon", "Casteless"]}
    native_charms = "Lunar"
    attribute_options = ["tier"]
    attribute_tier = "Normal: |w0|n, Favored: |w1|n, Caste: |w2|n"
    sheet_footer = "Lunars: The Stewards of Creation"

    @property
    def charm_categories(self):
        return self.game.attributes + ["Universal"]

    def calculate_pool_max_personal(self, target: "DefaultCharacter"):
        ess = self.get_advantage(target, "Essence")
        return ess + 15

    def calculate_pool_max_peripheral(self, target: "DefaultCharacter"):
        ess = self.get_advantage(target, "Essence")
        return 34 + (ess * 4)


class DragonBlooded(_Ex3Exalt):
    name = "Dragon-Blooded"
    fields = ["Aspect"]
    field_defaults = {"Aspect": "Air"}
    field_choices = {"Aspect": ["Air", "Earth", "Fire", "Water", "Wood"]}
    native_charms = "Dragon-Blooded"
    sheet_footer = "Dragon-Blooded: The Elemental Host"

    @property
    def charm_categories(self):
        return self.game.abilities

    def calculate_pool_max_personal(self, target: "DefaultCharacter"):
        ess = self.get_advantage(target, "Essence")
        return ess + 11

    def calculate_pool_max_peripheral(self, target: "DefaultCharacter"):
        ess = self.get_advantage(target, "Essence")
        return 23 + (ess * 4)


class Sidereal(_Ex3Exalt):
    fields = ["Caste"]
    field_defaults = {"Caste": "Journeys"}
    field_choices = {"Caste": ["Journeys", "Battles", "Secrets", "Endings", "Serenity"]}
    native_charms = "Sidereal"
    sheet_footer = "Sidereals: The Five-Score Fellowship"

    @property
    def charm_categories(self):
        return self.game.abilities + [
            "Journeys",
            "Battles",
            "Secrets",
            "Endings",
            "Serenity",
        ]

    def calculate_pool_max_personal(self, target: "DefaultCharacter"):
        ess = self.get_advantage(target, "Essence")
        return (ess * 2) + 9

    def calculate_pool_max_peripheral(self, target: "DefaultCharacter"):
        ess = self.get_advantage(target, "Essence")
        return 25 + (ess * 6)


class Abyssal(Solar):
    fields = ["Caste"]
    field_defaults = {"Caste": "Dusk"}
    field_choices = {"Caste": ["Dusk", "Midnight", "Daybreak", "Day", "Moonshadow"]}
    native_charms = "Abyssal"
    ability_tier = "Normal: |w0|n, Favored: |w1|n, Caste: |w2|n, Chthonic: |w3|n"
    ability_options = ["tier"]
    sheet_footer = "Abyssals: The Deathknights of the Underworld"


class Infernal(Solar):
    fields = ["Caste"]
    field_defaults = {"Caste": "Azimuth"}
    field_choices = {"Caste": ["Azimuth", "Ascendant", "Horizon", "Nadir", "Penumbra"]}
    native_charms = "Infernal"
    ability_tier = "Normal: |w0|n, Favored: |w1|n, Caste: |w2|n, Profane: |w3|n"
    ability_options = ["tier"]
    sheet_footer = "Infernals: The Green Sun Princes of Hell"


class Alchemical(_Ex3Exalt):
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
    attribute_options = ["tier"]
    attribute_tier = "Normal: |w0|n, Favored: |w1|n, Caste: |w2|n"
    sheet_footer = "Alchemicals: The Champions of the Great Maker"

    @property
    def charm_categories(self):
        return self.game.attributes


class Liminal(_Ex3Exalt):
    fields = ["Aspect"]
    field_defaults = {"Aspect": "Blood"}
    field_choices = {"Aspect": ["Blood", "Breath", "Flesh", "Marrow", "Soil"]}
    native_charms = "Liminal"
    sheet_footer = "Liminals: The Chernozem of the Dark Mother"

    @property
    def charm_categories(self):
        return self.game.attributes


class Getimian(_Ex3Exalt):
    fields = ["Caste"]
    field_defaults = {"Caste": "Spring"}
    field_choices = {"Caste": ["Spring", "Summer", "Autumn", "Winter"]}
    native_charms = "Getimian"
    sheet_footer = "Getimians: The Gambits of Rakan Thulio"

    @property
    def charm_categories(self):
        return self.game.attributes


class Exigent(_Ex3Exalt):
    fields = ["Tier", "Type", "Patron"]
    field_defaults = {"Tier": "Terrestrial", "Type": "Essence"}
    field_choices = {
        "Tier": ["Terrestrial", "Celestial"],
        "Type": ["Essence", "Attribute", "Ability"],
    }
    native_charms = "Exigent"
    sheet_footer = "Exigents: The Scions of the Gods"

    @property
    def charm_categories(self):
        return (
            self.game.attributes
            + self.game.abilities
            + _EXIGENT_CHARMS
            + ["Mysticism", "Universal", "Essence"]
        )


class Architect(_Ex3Exalt):
    fields = ["City"]
    native_charms = "Architect"
    sheet_footer = "Architects: The Chosen of City Fathers"

    @property
    def charm_categories(self):
        return self.game.attributes


class DreamSouled(_Ex3Exalt):
    name = "Dream-Souled"
    native_charms = "Dream-Souled"
    charm_categories = ["Illusion and Transformation"] + _EXIGENT_CHARMS
    sheet_footer = "Dream-Souled: The Chosen of the Wyld"


class Sovereign(_Ex3Exalt):
    native_charms = "Sovereign"
    sheet_footer = "Sovereigns: From the Font of Glories"

    @property
    def charm_categories(self):
        return self.game.abilities


class Hearteater(_Ex3Exalt):
    native_charms = "Hearteater"
    charm_categories = ["Pawn"] + _EXIGENT_CHARMS + ["Mysticism"]
    sheet_footer = "Hearteaters: Aurora's Cursed Chosen"


class Umbral(_Ex3Exalt):
    native_charms = "Umbral"
    charm_categories = ["Penumbra", "Darkness"] + _EXIGENT_CHARMS + ["Mysticism"]
    sheet_footer = "Umbrals: What Remains of Nebiru"


class _Spirit(_Ex3Template):
    native_charms = "Spirit"
    charm_categories = ["Universal"] + _EXIGENT_CHARMS + ["Essence", "Mysticism"]
    pools = ["Willpower", "Personal"]


class God(_Spirit):
    name = "God"
    fields = ["Purview"]
    sheet_footer = "Gods: The Celestial Bureaucracy"


class Elemental(_Spirit):
    name = "Elemental"
    fields = ["Element"]
    field_choices = {"Element": ["Air", "Earth", "Fire", "Water"]}
    sheet_footer = "Elementals: The Elemental Courts"


class Demon(_Spirit):
    name = "Demon"
    fields = ["Type", "Oversoul"]
    field_choices = {"Type": ["First Circle", "Second Circle", "Third Circle"]}
    field_Defaults = {"Type": "First Circle"}
    sheet_footer = "Demons: The Spawn of Malfeas"
