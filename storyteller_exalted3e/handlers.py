from django.conf import settings

from athanor.utils import partial_match, validate_name
import storyteller
from storyteller.utils import dramatic_capitalize

from storyteller.handlers import (
    StatHandler,
    PowerHandler,
    StatPowerHandler,
    CustomPowerHandler,
    AbilityHandler as _AbilityHandler,
)


class AbilityHandler(_AbilityHandler):
    pass


class StyleHandler(StatHandler):
    stat_category = "Styles"
    plural_name = "Martial Arts Styles"
    singular_name = "Martial Arts Style"
    remove_zero = True
    name = "Styles"
    options = ("set", "delete")

    def get_choice(self, entry: str) -> str:
        name = validate_name(entry, thing_type=self.singular_name)
        return dramatic_capitalize(name)


class XCharmHandler(PowerHandler):
    plural_name = "Charms"
    singular_name = "Charm"
    name = "XCharms"
    family = "Charms"

    def get_categories(self) -> list[str]:
        return list(storyteller.TEMPLATES.values())

    def get_category(self, name: str) -> str:
        if not name:
            raise ValueError(f"No {self.singular_name} category given.")
        choices = self.get_categories()
        if not (category := partial_match(name, choices)):
            raise ValueError(
                f"No {self.singular_name} category found matching '{name}'. Choices are: {', '.join(choices)}"
            )
        return category

    def get_subcategory(self, category: str, name: str) -> str:
        if not name:
            raise ValueError(f"No {category} {self.singular_name} category given.")
        choices = category.charm_categories

        if not (subcategory := partial_match(name, choices)):
            raise ValueError(
                f"No {category} {self.plural_name} subcategory found matching '{name}'. Choices are: {', '.join(choices)}"
            )

        return subcategory

    def render_name(self):
        return "Charms"

    def render_cat_name(self, category: str) -> str:
        return f"{category} Charms"

    def render_subcat_name(self, category: str, subcategory: str) -> str:
        return f"{category} {subcategory} Charms"

    def render_thing_name(self, category: str, subcategory: str, name: str) -> str:
        return f"{category} {subcategory} Charm: {name}"


class CharmHandler(XCharmHandler):
    name = "Charms"

    def prepare_args(self, path, value, method) -> list:
        path.insert(0, str(self.owner.st_template.get()))
        return super().prepare_args(path, value, method)


class MartialHandler(StatPowerHandler):
    name = "Martial"
    stat_category = "Styles"
    singular_name = "Martial Arts Charm"


class EvocationHandler(CustomPowerHandler):
    name = "Evocations"
    stat_category = "Merits"
    stat = "Artifact"
    singular_name = "Evocation"


class SpellHandler(PowerHandler):
    name = "Spells"
    category = "Spells"
    categories = {
        "Sorcery": ["Terrestrial", "Celestial", "Solar"],
        "Necromancy": ["Ivory", "Shadow", "Void"],
    }
    singular_name = "Spell"
    plural_name = "Spells"
    options = ("add", "remove", "tag", "untag")
    family = "Spells"

    def render_rank(self, rank) -> str:
        return f"{rank.power.subcategory} Circle {rank.power.category} {self.singular_name}: {rank.power.name}"
