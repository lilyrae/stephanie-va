import os
import configparser
import json


class Configurer:
    def __init__(self, filename="config.ini", modules_filename="modules.json"):
        self.abs_filename = self.get_abs_filename(filename)
        self.abs_mods_filename = self.get_abs_filename(modules_filename)
        self.config = configparser.ConfigParser()
        self.config.read(self.abs_filename)
        self.sections = self.config.sections()

    def init_modules(self):
        self.modules = self.retreive_modules(self.abs_mods_filename)

    @staticmethod
    def retreive_modules(abs_mods_filename):
        try:
            with open(abs_mods_filename, "r") as file:
                modules = json.load(file)
                file.close()
        except Exception as e:
            raise Exception(_("error.format_modules_file")) from e
        return modules

    def get_modules(self, filename=None):
        if filename:
            abs_mods_filename = self.get_abs_filename(filename)
            return self.retreive_modules(abs_mods_filename)
        return self.modules

    @staticmethod
    def get_abs_filename(filename):
        return os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            os.pardir, filename))


config = Configurer()
