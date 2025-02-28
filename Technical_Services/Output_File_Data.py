import pymongo
import gridfs

def output_file_data(database, filename):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client[database]
    fs = gridfs.GridFS(db)

    file_metadata = db.fs.files.find_one({"filename": filename})

    if file_metadata:
        file_data = fs.get(file_metadata['_id'])
        return file_data.read().decode()  # Assuming the file is a text file
    else:
        return f"File with filename '{filename}' not found."
