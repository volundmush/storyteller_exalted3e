def init(settings, plugins):
    settings.STORYTELLER_MODULES["EX3"] = (
        "storyteller_exalted3e.base.Exalted3e",
        "Exalted 3rd Edition",
        "EX3",
    )

    settings.STORYTELLER_DEFAULT_MODULE = "EX3"
