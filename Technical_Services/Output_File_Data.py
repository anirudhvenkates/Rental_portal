import pymongo
import gridfs

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']  # Replace with your database name

# Create a GridFS object
fs = gridfs.GridFS(db)

# The filename of the file you want to display
filename = 'your_filename.txt'  # Replace with your actual file name

# Find the file in GridFS using the filename
file_metadata = db.fs.files.find_one({"filename": filename})

# Check if file exists
if file_metadata:
    # Get the file object using the file_id
    file_data = fs.get(file_metadata['_id'])
    
    # Display the contents of the file
    print("File Content:")
    print(file_data.read().decode())  # Assuming the file is a text file, decode the bytes to a string
else:
    print("File not found")
