from Stephanie.configurer import config


# noinspection SpellCheckingInspection
class AudioRecognizer:
    def __init__(self, recognizer, UnknownValueError, RequestError):
        self.UnknownValueError = UnknownValueError
        self.RequestError = RequestError
        self.r = recognizer
        self.c = config

    def recognize_from_sphinx(self, audio):
        # recognize speech using Sphinx
        try:
            text = self.r.recognize_sphinx(audio)
            print(_("audio.repeat_input").format("Sphinx", text))
            return text
        except self.UnknownValueError:
            print(_("error.audio.failed_understand").format("Sphinx"))
            return False
        except self.RequestError as e:
            print(_("error.audio.failed_request_service").format("Sphinx", e))
            return False

    def recognize_from_google(self, audio):
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            text = self.r.recognize_google(audio)
            print(_("audio.repeat_input").format("Google Speech Recognition", text))
            return text
        except KeyError:
            print(_("error.audio.google_recognition.failed_understand"))
        except self.UnknownValueError:
            print(_("error.audio.failed_understand").format("Google Speech Recognition"))
            return False
        except self.RequestError as e:
            print(_("error.audio.failed_request_service").format("Google Speech Recognition", e))
            return False

    def recognize_from_google_cloud(self, audio):
        # recognize speech using Google Cloud Speech
        try:
            google_cloud_speech_credentials = self.c.config['STT_KEYS']['google_cloud_speech_api']
        except KeyError:
            print(_("error.missing_api_key"))
            return False
        try:
            text = self.r.recognize_google_cloud(audio,
                                                 credentials_json=google_cloud_speech_credentials)
            print(_("audio.repeat_input").format("Google Cloud Speech", text))
            return text
        except self.UnknownValueError:
            print(_("error.audio.failed_understand").format("Google Cloud Speech"))
            return False
        except self.RequestError as e:
            print(_("error.audio.failed_request_service").format("Google Cloud Speech", e))
            return False

    def recognize_from_wit(self, audio):
        # recognize speech using Wit.ai
        try:
            # Wit.ai keys are 32-character uppercase alphanumeric strings
            wit_ai_key = self.c.config['STT_KEYS']['wit.ai_speech_api']  
        except KeyError:
            print(_("error.missing_api_key"))
            return False
        try:
            text = self.r.recognize_wit(audio, key=wit_ai_key)
            print(_("audio.repeat_input").format("Wit.ai", text))
            return text
        except self.UnknownValueError:
            print(_("error.audio.failed_understand").format("Wit.ai"))
            return False
        except self.RequestError as e:
            print(_("error.audio.failed_request_service").format("Wit.ai", e))
            return False

    def recognize_from_bing(self, audio):
        # recognize speech using Microsoft Bing Voice Recognition
        # Microsoft Bing Voice Recognition API keys 32-character
        # lowercase hexadecimal strings
        try:
            bing_key = self.c.config['STT_KEYS']['bing_speech_api']
        except KeyError:
            print(_("error.missing_api_key"))
            return False
        try:
            text = self.r.recognize_bing(audio, key=bing_key)
            print(_("audio.repeat_input").format("Microsoft Bing Voice Recognition", text))
            return text
        except self.UnknownValueError:
            print(_("error.audio.failed_understand").format("Microsoft Bing Voice Recognition"))
            return False
        except self.RequestError as e:
            print(_("error.audio.failed_request_service").format("Microsoft Bing Voice Recognition", e))
            return False

    def recognize_from_houndify(self, audio):
        # recognize speech using Houndify
        try:
            # Houndify client IDs are Base64-encoded strings
            houndify_client_id = self.c.config['STT_KEYS']['houndify_client_id'] 
            # Houndify client keys are Base64-encoded strings
            houndify_client_key = self.c.config['STT_KEYS']['houndify_client_key']  
        except KeyError:
            print(_("error.missing_api_key"))
            return False
        try:
            text = self.r.recognize_houndify(audio, client_id=houndify_client_id,
                                             client_key=houndify_client_key)
            print(_("audio.repeat_input").format("Houndify", text))
            return text
        except self.UnknownValueError:
            print(_("error.audio.failed_understand").format("Houndify"))
            return False
        except self.RequestError as e:
            print(_("error.audio.failed_request_service").format("Houndify", e))
            return False

    def recognize_from_ibm(self, audio):
        # recognize speech using IBM Speech to Text
        try:
            # IBM Speech to Text usernames are strings of the
            # form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
            ibm_username = self.c.config['STT_KEYS']['ibm_username']
            # IBM Speech to Text passwords are mixed-case alphanumeric strings
            ibm_password = self.c.config['STT_KEYS']['ibm_password']
        except KeyError:
            print(_("error.missing_api_key"))
            return False
        try:
            text = self.r.recognize_ibm(audio, username=ibm_username,
                                        password=ibm_password)
            print(_("audio.repeat_input").format("IBM Speech to Text", text))
            return text
        except self.UnknownValueError:
            print(_("error.audio.failed_understand").format("IBM Speech to Text"))
            return False
        except self.RequestError as e:
            print(_("error.audio.failed_request_service").format("IBM Speech to Text", e))
            return False
