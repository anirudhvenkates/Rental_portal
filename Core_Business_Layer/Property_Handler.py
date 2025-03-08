from Technical_Services.File_Operations.FileHandler import FileHandler

class PropertyHandler:
    def __init__(self, session):
        self.session = session
        self.database_name = "users"
        self.file_handler = FileHandler(self.database_name)
        
    def operations(self):
        return ["1. Store a file","2. Output file data","3. Delete a file", "4. Retrieve file"]

    def perform_operations(self,choice):
        # Example file operations based on session details
        file_path = '/mnt/c/Users/anirudh.venkatesh/Desktop/Project/test_file.txt'
        output_file = 'output.json'
        filename = 'test_file.txt'

        # Store a file
        if choice == "Store a file":
            print(self.file_handler.store(file_path))  

        # Output file data (if needed)
        if choice == "Output file data":
            print(self.file_handler.output_data(filename))  

        # Delete a file
        if choice == "Delete a file":
            print(self.file_handler.delete(filename))
            
        # Retrieve file
        if choice == "Retrieve file":
            print(self.file_handler.retrieve(output_file))
