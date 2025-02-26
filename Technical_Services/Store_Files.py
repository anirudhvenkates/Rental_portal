import pymongo
import gridfs
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(description="Upload a file to MongoDB GridFS.")
parser.add_argument('database', type=str, help="The name of the MongoDB database.")
parser.add_argument('file_path', type=str, help="The path to the file to be uploaded.")
parser.add_argument('file_name', type=str, help="The name for the file in MongoDB.")

# Parse the arguments
args = parser.parse_args()

# Connect to MongoDB server
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Select your database
db = client[args.database]

# Create a GridFS object
fs = gridfs.GridFS(db)

# Open the file and store it in MongoDB using GridFS
with open(args.file_path, 'rb') as file_data:
    file_id = fs.put(file_data, filename=args.file_name)

print(f"File uploaded successfully with ID: {file_id}")