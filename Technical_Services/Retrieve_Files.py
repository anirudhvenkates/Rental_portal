import pymongo
import json
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(description="Retrieve files from MongoDB and export to JSON.")
parser.add_argument('database', type=str, help="The MongoDB database name.")
parser.add_argument('output_file', type=str, help="The name of the output JSON file.")

# Parse the arguments
args = parser.parse_args()

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client[args.database]  # Use the database from command line input

# Access the collection
collection = db['fs.files']  # Replace with the appropriate collection name

# Query the data (you can modify the query if needed)
files = collection.find()

# Open the output file and write the data
with open(args.output_file, 'w') as file:
    json.dump(list(files), file, default=str)  # Convert the MongoDB document to JSON format
    print(f"Data exported successfully to {args.output_file}")
