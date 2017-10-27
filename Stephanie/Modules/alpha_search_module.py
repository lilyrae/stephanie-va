from Stephanie.Modules.base_module import BaseModule
from Stephanie.local_libs.wolframalpha_speech.index import WolframalphaSpeech
from Stephanie.local_libs.wolframalpha_speech.exceptions_manager import *


class AlphaSearchModule(BaseModule):
    def __init__(self, *args):
        super(AlphaSearchModule, self).__init__(*args)
        self.app_id = self.get_configuration('wolframalpha_search_engine_key')
        if self.app_id:
            self.client = WolframalphaSpeech(self.app_id)
        else:
            return False

    def do_a_search(self):
        status = False
        phrase = ""
        raw_text_array = self.raw_text.split()
        end_index = len(raw_text_array)
        for i in range(0, end_index):
            if status:
                phrase += " " + raw_text_array[i]
            elif raw_text_array[i] == "search":
                status = True
        if status is False:
            return _("rephrase.ask")
        phrase = phrase.strip()
        try:
            text = self.client.search(phrase)
        except ConfidenceError:
            return _("error.search.no_results")
        except InternalError:
            return _("error.search.wolframalpha")
        except MissingTokenError:
            return _("error.search.no_api_token")
            print(_("error.search.wolframalpha.no_api_token"))
        except InvalidTokenError:
            return _("error.search.incorrect_api_token")
            print(_("error.search.wolframalpha.incorrect_api_token"))
        return text
