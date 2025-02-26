import pymongo
import gridfs
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(description="Retrieve and display a file's content from MongoDB GridFS.")
parser.add_argument('database', type=str, help="The name of the MongoDB database.")
parser.add_argument('filename', type=str, help="The filename of the file you want to retrieve.")

# Parse the arguments
args = parser.parse_args()

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client[args.database]  # Use the database name from the command-line argument

# Create a GridFS object
fs = gridfs.GridFS(db)

# Find the file in GridFS using the filename
file_metadata = db.fs.files.find_one({"filename": args.filename})

# Check if the file exists
if file_metadata:
    # Get the file object using the file_id
    file_data = fs.get(file_metadata['_id'])
    
    # Display the contents of the file
    print("File Content:")
    print(file_data.read().decode())  # Assuming the file is a text file, decode the bytes to a string
else:
    print(f"File with filename '{args.filename}' not found.")