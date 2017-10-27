import os
import eyed3
import time
from pygame import mixer
import platform


class Speaker:
    def __init__(self):
        self.speak_result = ""
        self.audio_file = None

    def speak_from_os(self, speech_result_filename):
        self.speak_result = self.get_abs_filename(speech_result_filename)
        try:
            self.speak_result = self.get_abs_filename(speech_result_filename)
            # Check platform used
            if platform.system() == "Linux":
                os.system("xdg-open " + self.speak_result)
            elif platform.system() == "Darwin":
                os.system("afplay " + self.speak_result)
            elif platform.system() == "Windows":
                os.startfile(self.speak_result)
            else:
                os.system(self.speak_result)
        except:
            print(_("error.speaker.default"))
        try:
            self.hibernate()
        except:
            print(_("error.eyed3_package.unknown"))

    @staticmethod
    def get_abs_filename(filename):
        speak_result = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                    os.pardir, filename))
        return speak_result

    def hibernate(self):
        self.audio_file = eyed3.load(self.speak_result)
        wait_period = self.audio_file.info.time_secs
        time.sleep(wait_period + 2)

    def say(self, speech):
        self.speak_from_os(speech)

    def speak_from_pygame(self, speech_result_filename):
        self.speak_result = self.get_abs_filename(speech_result_filename)
        try:
            self.speak_pygame()
        except:
            pass

    def speak_pygame(self):
        mixer.init()
        mixer.pause()
        mixer.music.load(self.speak_result)
        mixer.music.play()
        self.hibernate()
        mixer.music.stop()
        mixer.unpause()
        mixer.quit()
