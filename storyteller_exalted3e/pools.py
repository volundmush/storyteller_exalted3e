from storyteller.base import Pool


class _EX3Pool(Pool):
    can_commit = True


class _EssencePool(_EX3Pool):
    type_name_singular = "Essence"
    type_name_plural = "Essence"
    unit_name_singular = "Mote"
    unit_name_plural = "Motes"


class Personal(_EssencePool):
    pass


class Peripheral(_EssencePool):
    pass


class Willpower(_EX3Pool):
    type_name_singular = "Willpower"
    type_name_plural = "Willpower"


class Limit(_EX3Pool):
    pool_type = "Track"
    type_name_singular = "Limit"
    type_name_plural = "Limit"
    ignore_reset = True

    def calculate_max(self, target):
        return 10
