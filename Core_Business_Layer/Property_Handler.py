# Core_Business_Layer/Property_Handler.py

from Technical_Services.Store_Files import store_file
from Technical_Services.Retrieve_Files import retrieve_file
from Technical_Services.Output_File_Data import output_file_data
from Technical_Services.Delete_File import delete_file

def perform_operations(session, database_name):

    # Example file operations based on session details
    file_path = '/mnt/c/Users/anirudh.venkatesh/Desktop/Project/test_file.txt'

    print(store_file(database_name, file_path))  # Store a file
    print(retrieve_file(database_name, 'output.json'))  # Retrieve files
    print(output_file_data(database_name, 'test_file.txt'))  # Output file data
    print(delete_file(database_name, 'test_file.txt'))  # Delete a file
