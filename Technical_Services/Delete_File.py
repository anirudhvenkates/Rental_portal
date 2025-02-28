import pymongo
import gridfs

def delete_file(database, filename):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client[database]
    fs = gridfs.GridFS(db)

    file_metadata = db.fs.files.find_one({"filename": filename})

    if file_metadata:
        fs.delete(file_metadata['_id'])
        return f"File with filename '{filename}' has been deleted successfully."
    else:
        return f"File with filename '{filename}' not found."
