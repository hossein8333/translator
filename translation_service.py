from googletrans import Translator

class TranslationService:
    def translate(self, text, source_language, target_language):
        translator = Translator()
        translation = translator.translate(text, src=source_language, dest=target_language)
        return translation.text
