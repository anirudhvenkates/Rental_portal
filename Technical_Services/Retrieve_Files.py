import pymongo
import json

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']  # Replace with your database name

# Access the collection
collection = db['fs.files']  # Replace with the appropriate collection name

# Query the data (you can modify the query if needed)
files = collection.find()

# Open the output file and write the data
with open('output.json', 'w') as file:
    json.dump(list(files), file, default=str)  # Convert the MongoDB document to JSON format
    print("Data exported successfully to output.json")
