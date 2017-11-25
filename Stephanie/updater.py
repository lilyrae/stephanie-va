import requests
from Stephanie.configurer import config


class Updater:
    def __init__(self, speaker):
        self.speaker = speaker
        self.c = config
        self.current_version = self.c.config.get("APPLICATION", "version")
        self.update_url = "https://raw.githubusercontent.com/SlapBot/va-version-check/master/version.json"
        self.requests = requests
        self.data = None

    def check_for_update(self):
        try:
            self.data = self.get_update_information()
        except Exception:
            print(_("updater.error.failed_request"))
            return
        try:
            if str(self.current_version) != str(self.data['version']):
                print(_("updater.notice.old_version").format(
                    self.current_version,
                    self.data['version'])
                )
                if int(self.data['print_status']):
                    print(_("updater.notice.update_url"))
                if int(self.data['speak_status']):
                    self.speaker.speak(self.data['message'])
            for message in self.data['additional_information']:
                print(message)
            if self.data['speak_announcement']:
                self.speaker.speak(self.data['speak_announcement'])
        except Exception:
            print(_("updater.error.failed_update"))
            return

    def get_update_information(self):
        r = self.requests.get(self.update_url)
        data = r.json()
        return data
