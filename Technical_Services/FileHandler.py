from Technical_Services.Store_Files import store_file
from Technical_Services.Retrieve_Files import retrieve_file
from Technical_Services.Output_File_Data import output_file_data
from Technical_Services.Delete_File import delete_file

class FileHandler:
    def __init__(self, database_name):
        self.database_name = database_name

    def store(self, file_path):
        return store_file(self.database_name, file_path)
    
    def retrieve(self, output_file):
        return retrieve_file(self.database_name, output_file)
    
    def output_data(self, filename):
        return output_file_data(self.database_name, filename)
    
    def delete(self, filename):
        return delete_file(self.database_name, filename)
