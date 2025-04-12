# Core_Business_Layer/Enquiry_Handler.py

from Technical_Services.File_Operations.FileHandler import FileHandler
from Core_Business_Layer.NLP_Handler import NLPHandler

class EnquiryHandler:
    def __init__(self, session):
        self.session = session
        self.database_name = "users"
        self.file_handler = FileHandler(self.database_name)
        self.nlp_handler = NLPHandler()

    def operations(self):
        # Add your new operation for NLP-based property search
        return ["1. Search Properties"]

    def perform_operations(self, choice, file_info):
        # For the NLP-based search operation
        if choice == "Search Properties":
            # Process the natural language query from file_info (which now holds the user's query)
            query_params = self.nlp_handler.process_query(file_info)
            # Retrieve properties based on the extracted parameters.
            # (Here you should implement your property filtering logic using query_params.)
            properties = self.retrieve_properties(query_params)
            print(properties)
            return properties
        else:
            return "Invalid operation for customer."

    def retrieve_properties(self, query_params):
        """
        Stub for property retrieval.
        Replace this method with actual logic to query your database or data source using query_params.
        """
        # For now, just return a placeholder message
        return f"Retrieved properties with parameters: {query_params}"
