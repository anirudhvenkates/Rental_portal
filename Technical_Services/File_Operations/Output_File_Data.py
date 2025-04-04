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
    
    if output_format == "auto":
        if mime_type:
            if mime_type.startswith("text"):
                try:
                    return raw_data.decode('utf-8')
                except UnicodeDecodeError:
                    return "Error: Failed to decode text file with utf-8 encoding."
            elif mime_type.startswith("image"):
                # Encode image data in Base64 and prepend the proper data URL header.
                encoded = base64.b64encode(raw_data).decode('utf-8')
                return f"data:{mime_type};base64,{encoded}"
            else:
                # For other binary files, return the base64-encoded data.
                return base64.b64encode(raw_data).decode('utf-8')
        else:
            try:
                return raw_data.decode('utf-8')
            except UnicodeDecodeError:
                return base64.b64encode(raw_data).decode('utf-8')
    elif output_format == "raw":
        return raw_data
    elif output_format == "base64":
        return base64.b64encode(raw_data).decode('utf-8')
    else:
        return "Unsupported output format."
