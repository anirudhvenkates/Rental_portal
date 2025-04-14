# Core_Business_Layer/Property_Handler.py
from Technical_Services.File_Operations.FileHandler import FileHandler

class PropertyHandler:
    def __init__(self, session):
        self.session = session
        self.database_name = "users"
        self.file_handler = FileHandler(self.database_name)

    def operations(self):
        # Add a new operation for storing house images
        return ["1. Store a House Image", "2. Output file data", "3. Delete a file", "4. Retrieve file"]

    def perform_operations(self, choice, file_info):
        # For storing a house image, parse the file_info string into a dictionary.
        if choice == "Store a House Image":
            # If file_info is provided as a string, parse it into a dictionary.
            if isinstance(file_info, str) and file_info.strip() != "":
                info_dict = self.parse_file_info(file_info)
                if "file_path" in info_dict:
                    metadata = {k: v for k, v in info_dict.items() if k != "file_path"}
                    result = self.file_handler.store(info_dict["file_path"], metadata=metadata)
                    print(result)
                    return result
                else:
                    return "Error: file_path not provided in the input."
            else:
                return "Invalid file info provided for storing house image."

        # Output file data
        if choice == "Output file data":
            result = self.file_handler.output_data(file_info)
            print(result)
            return result 

        # Delete a file
        if choice == "Delete a file":
            result = self.file_handler.delete(file_info)
            print(result)
            return result

        # Retrieve file
        if choice == "Retrieve file":
            output_file = 'output.json'
            result = self.file_handler.retrieve(output_file)
            print(result)
            return result

    def parse_file_info(self, file_info_str):
        """
        Parses a string of the following format:
          file_path <file_path> house_type <house_type> bedrooms <number>

        For example:
          file_path /home/user/image.jpg house_type apartment bedrooms 3
        """
        tokens = file_info_str.split()
        result = {}
        key = None
        value_tokens = []
        for token in tokens:
            # Check if the token is one of the expected keys
            if token in ["file_path", "house_type", "bedrooms"]:
                if key is not None:
                    # Save the previous key's value as the join of value_tokens.
                    result[key] = " ".join(value_tokens)
                key = token
                value_tokens = []
            else:
                value_tokens.append(token)
        # Save the final key if any.
        if key is not None:
            result[key] = " ".join(value_tokens)
        # For "bedrooms", convert the value to an integer if possible.
        if "bedrooms" in result:
            try:
                result["bedrooms"] = int(result["bedrooms"])
            except ValueError:
                pass
        return result
