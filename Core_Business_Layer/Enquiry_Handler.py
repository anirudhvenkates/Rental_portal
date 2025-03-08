from Technical_Services.File_Operations.FileHandler import FileHandler

class EnquiryHandler:
    def __init__(self, session):
        self.session = session
        self.database_name = "users"
        # Initialize the FileHandler with the database name
        self.file_handler = FileHandler(self.database_name)
        
    def operations(self):
        return ["1. Output file data"]

    def perform_operations(self, choice):
        # If the user is a customer, they can only output file data
        # Output file data (if needed)
        if choice == "Output file data":
            print(self.file_handler.output_data('test_file.txt'))
        else:
            return "Invalid operation for customer."
