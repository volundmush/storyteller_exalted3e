from django.conf import settings

from athanor.utils import partial_match, validate_name
import storyteller
from storyteller.utils import dramatic_capitalize

from storyteller.handlers import (
    StatHandler as _StatHandler,
    PowerHandler as _PowerHandler,
    StatPowerHandler as _StatPowerHandler,
    CustomPowerHandler as _CustomPowerHandler,
    TemplateHandler as _TemplateHandler,
    FieldHandler as _FieldHandler,
    AttributeHandler as _AttributeHandler,
    AbilityHandler as _AbilityHandler,
    SpecialtyHandler as _SpecialtyHandler,
    MeritHandler as _MeritHandler,
    FlawHandler as _FlawHandler,
)


class TemplateHandler(_TemplateHandler):
    pass


class FieldHandler(_FieldHandler):
    pass


class AttributeHandler(_AttributeHandler):
    @property
    def options(self):
        t = self.template()
        out = ["set", "rank"]
        if extra := getattr(t, "attribute_options", None):
            out.extend(extra)
        return set(out)

    def render_help_extra(self, lines):
        super().render_help_extra(lines)
        t = self.template()
        if tier := getattr(t, "attribute_tier", None):
            lines.append(f"  |wTier|n: {tier}")


class AbilityHandler(_AbilityHandler):
    options = ("set", "rank", "tier")

    @property
    def options(self):
        t = self.template()
        out = ["set", "rank"]
        if extra := getattr(t, "ability_options", None):
            out.extend(extra)
        return set(out)

    def render_help_extra(self, lines):
        super().render_help_extra(lines)
        t = self.template()
        if tier := getattr(t, "ability_tier", None):
            lines.append(f"  |wTier|n: {tier}")


class SpecialtyHandler(_SpecialtyHandler):
    pass


class MeritHandler(_MeritHandler):
    pass


class FlawHandler(_FlawHandler):
    pass


class StyleHandler(_StatHandler):
    stat_category = "Styles"
    plural_name = "Martial Arts Styles"
    singular_name = "Martial Arts Style"
    remove_zero = True
    name = "Styles"
    options = ("set", "delete")
    load_order = 21
    dynamic_choices = True


class _BaseCharmHandler(_PowerHandler):
    plural_name = "Charms"
    singular_name = "Charm"
    load_order = 60

    def get_choices(self) -> list[str]:
        return list(self.game.templates.values())

    def get_subcategory_choices(self, operation, category: str):
        t = self.game.templates.get(category)
        return t.charm_categories

    def render_name(self):
        return "Charms"

    def render_cat_name(self, category: str) -> str:
        return f"{category} Charms"

    def render_subcat_name(self, category: str, subcategory: str) -> str:
        return f"{category} {subcategory} Charms"

    def render_thing_name(self, category: str, subcategory: str, name: str) -> str:
        return f"{category} {subcategory} Charm: {name}"


class OtherCharmHandler(_BaseCharmHandler):
    name = "OtherCharms"
    family = "Charms"
    load_order = 62


class NativeCharmHandler(_BaseCharmHandler):
    name = "NativeCharms"
    load_order = 61

    def modify_path(self, path):
        path.insert(0, str(self.template().name))

    def render_help_choices(self, lines):
        t = self.template().name
        if choices := self.game.templates.get(t).charm_categories:
            lines.append(f"  |wChoices|n: {', '.join([str(x) for x in choices])}")


class MartialHandler(_StatPowerHandler):
    name = "MartialArtsCharms"
    stat_category = "Styles"
    singular_name = "Martial Arts Charm"
    load_order = 63


class EvocationHandler(_CustomPowerHandler):
    name = "Evocations"
    stat_category = "Merits"
    stat = "Artifact"
    singular_name = "Evocation"
    load_order = 64


class _SpellHandler(_PowerHandler):
    category = "Spells"
    categories = {
        "Sorcery": ["Terrestrial", "Celestial", "Solar"],
        "Necromancy": ["Ivory", "Shadow", "Void"],
    }
    singular_name = "Spell"
    options = ("add", "remove", "tier")
    family = "Spells"
    load_order = 100

    def modify_path(self, path):
        path.insert(0, self.name)

    def get_choices(self):
        return list(self.categories.keys())

    def get_subcategory_choices(self, operation, category: str):
        return self.categories.get(category)

    def render_help_choices(self, lines):
        if choices := self.categories.get(self.name, None):
            lines.append(f"  |wChoices|n: {', '.join([str(x) for x in choices])}")

    def render_help_extra(self, lines):
        super().render_help_extra(lines)
        lines.append(f"  |wTier|n: Normal: |w0|n, Control: |w1|n")


class SorceryHandler(_SpellHandler):
    name = "Sorcery"


class NecromancyHandler(_SpellHandler):
    name = "Necromancy"
    load_order = 101
