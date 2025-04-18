# Technical_Services/File_Operations/FileHandler.py
from Technical_Services.File_Operations.Store_Files import store_file
from Technical_Services.File_Operations.Retrieve_Files import retrieve_file
from Technical_Services.File_Operations.Output_File_Data import output_file_data
from Technical_Services.File_Operations.Delete_File import delete_file
from Technical_Services.File_Operations.Property_Retriever import retrieve_properties

class FileHandler:
    def __init__(self, database_name):
        self.database_name = database_name

    def store(self, file_path, metadata=None):
        return store_file(self.database_name, file_path, metadata)
    
    def retrieve(self, output_file):
        return retrieve_file(self.database_name, output_file)
    
    def output_data(self, filename):
        return output_file_data(self.database_name, filename)
    
    def delete(self, filename):
        return delete_file(self.database_name, filename)
        
    def retrieve_properties(self, query_params):
        return retrieve_properties(self.database_name, query_params)
