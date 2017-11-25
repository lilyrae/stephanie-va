from urllib.request import Request, urlopen
from urllib.error import URLError
import json
from Stephanie.Modules.base_module import BaseModule
from Stephanie.language import lang


class WikipediaModule(BaseModule):
    def __init__(self, *args):
        super(WikipediaModule, self).__init__(*args)

    def give_a_summary(self):
        self.assistant.say(_("encyclopedia.search.ask"))
        text = self.assistant.listen().decipher()
        text = text.strip().replace(" ", "%20")
        request = Request(
            'https://' + lang.get_code() + '.wikipedia.org/w/api.php?'
            'format=json&action=query&prop=extracts&exintro=&explaintext=&titles=' + text
        )
        try:
            response = urlopen(request)
            data = json.loads(
                response.read().decode(
                    response.info().get_param('charset') or 'utf-8'
                )
            )
            output = data["query"]["pages"]

            # check that the content of output contains a page or not
            if list(output.keys())[0] is not '-1':
                final = output[list(output.keys())[0]]["extract"]
                return final
            else:
                self.assistant.say(_("encyclopedia.search.no_results"))
                return None

            return final

        except URLError:
            return _("error.encyclopedia.search")
