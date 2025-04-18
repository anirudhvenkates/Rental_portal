import re
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

class NLPHandler:
    def __init__(self):
        # existing mappings…
        self.property_types = {
            "apartment": {"apartment", "flat", "condo", "condominium"},
            "house": {"house", "home", "residence"},
            "villa": {"villa"},
        }
        self.amenities = {"garden", "balcony", "pool", "garage"}
        self.lemmatizer = WordNetLemmatizer()

        # For state extraction: lowercase names + USPS abbreviations
        state_names = [
            "alabama","alaska","arizona","arkansas","california","colorado","connecticut",
            # … include all 50 states …
            "wyoming"
        ]
        state_abbr = [abbr.lower() for abbr in [
            "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA",
            "KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
            "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT",
            "VA","WA","WV","WI","WY"
        ]]
        self.states = set(state_names + state_abbr)

    def lemmatize_tokens(self, tokens):
        return [self.lemmatizer.lemmatize(token) for token in tokens]

    def get_synonyms(self, word):
        synonyms = set()
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name().lower())
        return synonyms

    def match_property_type(self, tokens):
        for token in tokens:
            token_syns = self.get_synonyms(token) | {token}
            for standard, syn_set in self.property_types.items():
                if token_syns & syn_set:
                    return standard
        return None

    def extract_bedrooms(self, text):
        m = re.search(r'(\d+)\s*bed(room)?s?', text)
        return int(m.group(1)) if m else None

    def extract_amenities(self, tokens):
        found = []
        for token in tokens:
            if token in self.amenities:
                found.append(token)
            else:
                syns = self.get_synonyms(token)
                for amen in self.amenities:
                    if amen in syns:
                        found.append(amen)
                        break
        return list(set(found)) if found else None

    def extract_address(self, text):
        """
        Very basic street‐address puller: number + street name + type
        e.g. "123 Main St", "456 Elm Boulevard"
        """
        pattern = r'\b\d+\s+[A-Za-z0-9\s]+(?:Street|St|Road|Rd|Avenue|Ave|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Way|Terrace|Ter)\b'
        m = re.search(pattern, text, re.IGNORECASE)
        return m.group(0).strip() if m else None

    def extract_city(self, text):
        """
        Grabs what follows 'in <City>' up to a comma or end‑of‑string.
        """
        m = re.search(r'\bin\s+([A-Za-z\s]+?)(?:,|$)', text)
        return m.group(1).strip().title() if m else None

    def extract_state(self, tokens):
        """
        Finds any token matching a state name or USPS abbreviation.
        """
        for token in tokens:
            if token in self.states:
                return token.upper() if len(token)==2 else token.title()
        return None

    def extract_zip_code(self, text):
        """
        U.S. ZIP code: five digits (optionally + -four)
        """
        m = re.search(r'\b\d{5}(?:-\d{4})?\b', text)
        return m.group(0) if m else None

    def process_query(self, query):
        q_lower = query.lower()
        tokens = word_tokenize(q_lower)
        pos_tags = pos_tag(tokens)
        lemmas = self.lemmatize_tokens(tokens)

        params = {}
        pt = self.match_property_type(lemmas)
        if pt:
            params['property_type'] = pt
        br = self.extract_bedrooms(q_lower)
        if br is not None:
            params['bedrooms']= br
        am = self.extract_amenities(lemmas)
        if am:
            params['amenities'] = am
        addr = self.extract_address(query)
        if addr:
            params['address'] = addr

        city = self.extract_city(query)
        if city:
            params['city']= city

        st = self.extract_state(lemmas)
        if st:
            params['state']= st

        zc = self.extract_zip_code(query)
        if zc:
            params['zip_code']= zc
        return params


# Example usage for testing
if __name__ == "__main__":
    nlp_handler = NLPHandler()
    test_query = "Looking for a 3 bedroom apartment at 123 Main St in San Francisco, CA 94105 with a balcony"
    print("Extracted parameters:", nlp_handler.process_query(test_query))
