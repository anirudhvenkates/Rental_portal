from Technical_Services.FileHandler import FileHandler

def perform_operations(session, database_name):
    # Example file operations based on session details
    file_path = '/mnt/c/Users/anirudh.venkatesh/Desktop/Project/test_file.txt'
    output_file = 'output.json'
    filename = 'test_file.txt'

    # Create a FileHandler instance
    file_handler = FileHandler(database_name)

    # Store a file
    print(file_handler.store(file_path))  

    # Retrieve files
    #print(file_handler.retrieve(output_file))  
    
    # Output file data (if needed)
    print(file_handler.output_data(filename))  
    
    # Delete a file
    print(file_handler.delete(filename))  
