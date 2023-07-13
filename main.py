from language_recognizer import LanguageRecognizer
from translation_service import TranslationService
from country_detector import CountryDetector

def main():
    text = input("Enter the text: ")
    recognizer = LanguageRecognizer()
    language = recognizer.recognize_language(text)
    
    detector = CountryDetector()
    country = detector.get_country(language)
    
    target_language = input("Enter the target language: ")
    
    translator = TranslationService()
    translated_text = translator.translate(text, language, target_language)
    
    print(f"Detected language: {language}")
    print(f"Associated country: {country}")
    print(f"Translated text: {translated_text}")

if __name__ == "__main__":
    main()
