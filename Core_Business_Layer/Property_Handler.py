from Technical_Services.FileHandler import FileHandler

class PropertyHandler:
    def __init__(self, session, database_name):
        self.session = session
        self.database_name = database_name
        self.file_handler = FileHandler(database_name)

    def perform_operations(self):
        # Example file operations based on session details
        file_path = '/mnt/c/Users/anirudh.venkatesh/Desktop/Project/test_file.txt'
        output_file = 'output.json'
        filename = 'test_file.txt'

        # Store a file
        print(self.file_handler.store(file_path))  

        # Output file data (if needed)
        print(self.file_handler.output_data(filename))  

        # Delete a file
        print(self.file_handler.delete(filename))  
