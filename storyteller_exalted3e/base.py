from evennia.utils.utils import lazy_property
from storyteller.base import Game


class Exalted3e(Game):
    def __init__(self, alias: str, name: str, key: str = None):
        super().__init__(alias, name, key=key)
        self.setup_handlers("storyteller_exalted3e.handlers")
        self.setup_templates("storyteller_exalted3e.templates")
        self.setup_pools("storyteller_exalted3e.pools")
        self.abilities = [
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
        self.physical_attributes = ["Strength", "Dexterity", "Stamina"]
        self.social_attributes = ["Charisma", "Manipulation", "Appearance"]
        self.mental_attributes = ["Perception", "Intelligence", "Wits"]

    @lazy_property
    def attributes(self):
        return (
            self.physical_attributes + self.social_attributes + self.mental_attributes
        )
