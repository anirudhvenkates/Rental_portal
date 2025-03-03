import pymongo
import json

def retrieve_file(database, output_file):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client[database]
    collection = db['fs.files']

    files = collection.find()

    with open(output_file, 'w') as file:
        json.dump(list(files), file, default=str)

    return f"Data exported successfully to {output_file}"
