from Technical_Services.File_Operations.FileHandler import FileHandler
from Core_Business_Layer.NLP_Handler import NLPHandler

class EnquiryHandler:
    def __init__(self, session):
        self.logger = session['logger']
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
            self.logger.info("Processed NLP Query: " + str(query_params))
            # Retrieve properties based on the extracted parameters.
            properties = self.file_handler.retrieve_properties(query_params)
            self.logger.info("Retrieve Property Information")
            print(properties)
            return properties
        else:
            self.logger.error("Invalid Operation for Customer")
            return "Invalid operation for customer."
