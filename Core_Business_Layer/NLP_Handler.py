import re

class NLPHandler:
    def __init__(self):
        # Define some basic keywords for house types
        self.house_types = ['apartment', 'house', 'villa', 'condo']

    def process_query(self, query):
        """
        Process the natural language query and extract search parameters.
        
        Example:
            "I need a 3 bedroom apartment with a garden" ->
                {'house_type': 'apartment', 'bedrooms': 3}
        """
        query_lower = query.lower()
        params = {}

        # Detect house type by checking if any of the keywords are in the query
        for ht in self.house_types:
            if ht in query_lower:
                params['house_type'] = ht
                break

        # Extract number of bedrooms using a regex
        bedroom_match = re.search(r'(\d+)\s*bed(room)?s?', query_lower)
        if bedroom_match:
            params['bedrooms'] = int(bedroom_match.group(1))

        # You can add additional rules here to extract more parameters (e.g., location, amenities)

        return params

# Example usage for testing
if __name__ == "__main__":
    nlp = NLPHandler()
    test_query = "I am looking for a 3 bedroom apartment with a garden"
    print("Extracted parameters:", nlp.process_query(test_query))
