from Technical_Services.File_Operations.FileHandler import FileHandler
from Core_Business_Layer.NLP_Handler import NLPHandler
# Import the new property retriever function
from Technical_Services.Property_Retriever import retrieve_properties as ts_retrieve_properties

class EnquiryHandler:
    def __init__(self, session):
        self.session = session
        # You might want to use a separate database name for properties or use the same,
        # adjust accordingly.
        self.database_name = "users"  # or change to "propertiesdb" if needed
        self.file_handler = FileHandler(self.database_name)
        self.nlp_handler = NLPHandler()

    def operations(self):
        # Add your new operation for NLP-based property search
        return ["1. Search Properties"]

    def perform_operations(self, choice, file_info):
        # For the NLP-based search operation
        if choice == "Search Properties":
            # Process the natural language query from file_info
            query_params = self.nlp_handler.process_query(file_info)
            # Retrieve properties based on the extracted parameters.
            properties = self.retrieve_properties(query_params)
            print(properties)
            return properties
        else:
            return "Invalid operation for customer."

    def retrieve_properties(self, query_params):
        """
        Uses the technical services layer to retrieve properties based on query_params.
        """
        return ts_retrieve_properties(self.database_name, query_params)
