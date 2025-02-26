import pymongo
import gridfs

# Connect to MongoDB server
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Select your database
db = client['mydatabase']

# Create a GridFS object
fs = gridfs.GridFS(db)

# Path to your file
file_path = '/mnt/c/Users/anirudh.venkatesh/Desktop/Project/Rental_portal/README.md'

# Open the file and store it in MongoDB using GridFS
with open(file_path, 'rb') as file_data:
    file_id = fs.put(file_data, filename='your_filename.txt')

print(f"File uploaded successfully with ID: {file_id}")
