from Stephanie.configurer import config


class Language:

    _languages = {
        "en": "English",
        "it": "Italiano",
    }

    _default = "en"

    def __init__(self):
        config_language = config.config.get("SYSTEM", "language")

        if(config_language in Language._languages):
            self.system_language = config_language
        else:
            self.system_language = Language._default

    def get_code(self):
        return self.system_language

    def get_name(self):
        return Language._languages[self.system_language]

lang = Language()
