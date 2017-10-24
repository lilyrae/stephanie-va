from urllib.request import Request, urlopen
from urllib.error import URLError
import json
from Stephanie.Modules.base_module import BaseModule
from Stephanie.language import lang
from pprint import pprint

class WikipediaModule(BaseModule):
    def __init__(self, *args):
        super(WikipediaModule, self).__init__(*args)

    def give_a_summary(self):
        # Translate this \/
        self.assistant.say(_("What would you like to know about?"))
        text = self.assistant.listen().decipher()
        # add beep sound
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
            if list(output.keys())[0] is not '-1': # some page has been found
                final = output[list(output.keys())[0]]["extract"]
                return final
            else:
                # Translate this \/
                self.assistant.say(_("Sorry, I couldn't find any article with that title. :sadface:"))
                return None
            
            # handle final being None if the page wasn't found
            return final

        except URLError:
            return _("Unable to search your given query.")
