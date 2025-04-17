import re
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

class NLPHandler:
    def __init__(self):
        # Define a mapping of property types with known synonyms.
        self.property_types = {
            "apartment": {"apartment", "flat", "condo", "condominium"},
            "house": {"house", "home", "residence"},
            "villa": {"villa"},
            # You can add more property types and synonyms here
        }
        # Define a set for amenities. Add more as needed.
        self.amenities = {"garden", "balcony", "pool", "garage"}
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_tokens(self, tokens):
        """Reduce tokens to their base forms."""
        return [self.lemmatizer.lemmatize(token) for token in tokens]

    def get_synonyms(self, word):
        """Retrieve synonyms for a word using WordNet."""
        synonyms = set()
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name().lower())
        return synonyms

    def match_property_type(self, tokens):
        """
        Check if any token or its synonyms match any of our defined property types.
        Returns the standardized property type (e.g., "apartment") if found.
        """
        for token in tokens:
            # Get all synonyms for the token including the token itself.
            token_synonyms = self.get_synonyms(token) | {token}
            for standard, syn_set in self.property_types.items():
                # If there is any intersection between token synonyms and our property type synonyms.
                if token_synonyms.intersection(syn_set):
                    return standard
        return None

    def extract_bedrooms(self, text):
        """
        Extract the number of bedrooms using regex.
        Look for phrases like "3 bedroom" or "3 bedrooms".
        """
        bedroom_match = re.search(r'(\d+)\s*bed(room)?s?', text)
        if bedroom_match:
            return int(bedroom_match.group(1))
        return None

    def extract_amenities(self, tokens):
        """
        Extract amenities such as garden, balcony, etc. by checking
        if any tokens or their synonyms match the defined amenities.
        """
        detected = []
        for token in tokens:
            # Direct match against the token.
            if token in self.amenities:
                detected.append(token)
            else:
                # Check if synonyms contain any of our desired amenities.
                token_synonyms = self.get_synonyms(token)
                for amenity in self.amenities:
                    if amenity in token_synonyms:
                        detected.append(amenity)
                        break
        return list(set(detected)) if detected else None

    def process_query(self, query):
        """
        Process the query to extract property type, number of bedrooms, and amenities.
        Example: "I need a 3 bedroom flat with a garden and balcony"
                 => {'property_type': 'apartment', 'bedrooms': 3, 'amenities': ['garden', 'balcony']}
        """
        # Normalize query to lowercase.
        query_lower = query.lower()
        
        # Tokenize the query and perform POS tagging.
        tokens = word_tokenize(query_lower)
        pos_tags = pos_tag(tokens)
        
        # Lemmatize tokens for normalization.
        lemmatized_tokens = self.lemmatize_tokens(tokens)

        params = {}

        # Identify property type using synonym matching.
        property_type = self.match_property_type(lemmatized_tokens)
        if property_type:
            params['property_type'] = property_type

        # Extract bedroom information using regex.
        bedrooms = self.extract_bedrooms(query_lower)
        if bedrooms is not None:
            params['bedrooms'] = bedrooms

        # Extract amenities such as garden or balcony.
        amenities = self.extract_amenities(lemmatized_tokens)
        if amenities:
            params['amenities'] = amenities

        # Optional: Print debug information if needed.
        # print("Tokens:", tokens)
        # print("POS Tags:", pos_tags)
        # print("Lemmatized Tokens:", lemmatized_tokens)

        return params

# Example usage for testing
if __name__ == "__main__":
    nlp_handler = NLPHandler()
    test_query = "I need a 3 bedroom flat with a garden and balcony"
    print("Extracted parameters:", nlp_handler.process_query(test_query))
