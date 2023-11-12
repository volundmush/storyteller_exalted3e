def init(settings, plugins):
    settings.STORYTELLER_GAMES["EX3"] = (
        "storyteller_exalted3e.base.Exalted3e",
        "Exalted 3rd Edition",
        "EX3",
    )

    settings.STORYTELLER_DEFAULT_GAME = "EX3"
