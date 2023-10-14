from evennia.utils import lazy_property
from storyteller.characters import StorytellerCharacter as _StorytellerCharacter
from storyteller.handlers import (
    AdvantageHandler,
    SpecialtyHandler,
    TemplateHandler,
    FieldHandler,
    AttributeHandler,
)
from storyteller.handlers import MeritHandler, FlawHandler
from ..handlers import (
    AbilityHandler,
    StyleHandler,
    XCharmHandler,
    CharmHandler,
    SpellHandler,
    EvocationHandler,
    MartialHandler,
)


class Ex3Character(_StorytellerCharacter):
    story_handlers = [
        "st_template",
        "st_fields",
        "st_advantages",
        "st_attributes",
        "st_abilities",
        "st_specialties",
        "st_styles",
        "st_merits",
        "st_flaws",
        "st_xcharms",
        "st_charms",
        "st_spells",
        "st_evocations",
        "st_martial",
    ]

    @lazy_property
    def st_template(self):
        return TemplateHandler(self)

    @lazy_property
    def st_fields(self):
        return FieldHandler(self)

    @lazy_property
    def st_advantages(self):
        return AdvantageHandler(self)

    @lazy_property
    def st_attributes(self):
        return AttributeHandler(self)

    @lazy_property
    def st_abilities(self):
        return AbilityHandler(self)

    @lazy_property
    def st_specialties(self):
        return SpecialtyHandler(self)

    @lazy_property
    def st_styles(self):
        return StyleHandler(self)

    @lazy_property
    def st_merits(self):
        return MeritHandler(self)

    @lazy_property
    def st_flaws(self):
        return FlawHandler(self)

    @lazy_property
    def st_charms(self):
        return CharmHandler(self)

    @lazy_property
    def st_xcharms(self):
        return XCharmHandler(self)

    @lazy_property
    def st_spells(self):
        return SpellHandler(self)

    @lazy_property
    def st_evocations(self):
        return EvocationHandler(self)

    @lazy_property
    def st_martial(self):
        return MartialHandler(self)
