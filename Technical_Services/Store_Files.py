import pymongo
import gridfs
import os

def store_file(database, file_path):
    # Extract the file name from the file path
    file_name = os.path.basename(file_path)

    # Connect to MongoDB server
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client[database]
    fs = gridfs.GridFS(db)

    # Open the file and store it in MongoDB using GridFS
    with open(file_path, 'rb') as file_data:
        file_id = fs.put(file_data, filename=file_name)

    return f"File uploaded successfully with ID: {file_id}"
