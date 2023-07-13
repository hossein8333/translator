class CountryDetector:
    def get_country(self, language):
        # Mapping of languages to countries
        language_country_map = {
            "en": "United States",
            "es": "Spain",
            "fr": "France",
            # Add more language-country mappings here
        }
        
        return language_country_map.get(language, "Unknown")
