from Technical_Services.Delete_File import delete_file
from Technical_Services.Store_Files import store_file
from Technical_Services.Retrieve_Files import retrieve_file
from Technical_Services.Output_File_Data import output_file_data

def perform_operations():
    # Example use cases, pass the parameters according to your needs
    database_name = 'mydatabase'

    # File path to be uploaded
    file_path = '/mnt/c/Users/anirudh.venkatesh/Desktop/Project/test_file.txt'

    # Store a file (the file name will be extracted from the file path)
    print(store_file(database_name, file_path))

    # Retrieve file data and export to JSON
    print(retrieve_file(database_name, 'output.json'))

    # Output file data
    print(output_file_data(database_name, 'test_file.txt'))

    # Delete a file
    print(delete_file(database_name, 'test_file.txt'))

if __name__ == '__main__':
    perform_operations()
