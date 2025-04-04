import pymongo
import gridfs
import mimetypes
import base64

def output_file_data(database, filename, output_format="auto"):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client[database]
    fs = gridfs.GridFS(db)

    file_metadata = db.fs.files.find_one({"filename": filename})
    if not file_metadata:
        return f"File with filename '{filename}' not found."
    
    file_data_obj = fs.get(file_metadata['_id'])
    raw_data = file_data_obj.read()
    
    # Guess the MIME type using the file extension
    mime_type, _ = mimetypes.guess_type(filename)
    
    # Decide how to handle the file based on MIME type
    if output_format == "raw":
        # Return raw bytes for further processing
        return raw_data

    # For auto mode, if the MIME type starts with "text", assume it's a text file
    if output_format == "auto":
        if mime_type and mime_type.startswith("text"):
            try:
                return raw_data.decode('utf-8')
            except UnicodeDecodeError:
                # Optionally try a different encoding or return an error message
                return "Error: Failed to decode text file with utf-8 encoding."
        else:
            # For binary files, encode in base64 to safely represent the data as text
            return base64.b64encode(raw_data).decode('utf-8')
    
    # If a specific output_format like "base64" is requested:
    if output_format == "base64":
        return base64.b64encode(raw_data).decode('utf-8')
    
    return "Unsupported output format."
