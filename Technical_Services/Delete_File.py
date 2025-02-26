import pymongo
import gridfs

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']  # Replace with your database name

# Create a GridFS object
fs = gridfs.GridFS(db)

# The filename of the file you want to delete
filename = 'your_filename.txt'  # Replace with the actual file name

# Find the file metadata using the filename
file_metadata = db.fs.files.find_one({"filename": filename})

# Check if the file exists
if file_metadata:
    # Delete the file using its _id
    fs.delete(file_metadata['_id'])
    print(f"File with filename '{filename}' has been deleted successfully.")
else:
    print(f"File with filename '{filename}' not found.")
