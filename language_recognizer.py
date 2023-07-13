from langdetect import detect

class LanguageRecognizer:
    def recognize_language(self, text):
        return detect(text)
