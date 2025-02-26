import pymongo
import gridfs
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(description="Delete a file from MongoDB GridFS.")
parser.add_argument('database', type=str, help="The name of the MongoDB database.")
parser.add_argument('filename', type=str, help="The filename of the file you want to delete.")

# Parse the arguments
args = parser.parse_args()

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client[args.database]  # Use the database name from the command-line argument

# Create a GridFS object
fs = gridfs.GridFS(db)

# Find the file metadata using the filename
file_metadata = db.fs.files.find_one({"filename": args.filename})

# Check if the file exists
if file_metadata:
    # Delete the file using its _id
    fs.delete(file_metadata['_id'])
    print(f"File with filename '{args.filename}' has been deleted successfully.")
else:
    print(f"File with filename '{args.filename}' not found.")