import pymongo
import gridfs
import mimetypes
import base64

def output_file_data(database, filename, output_format="auto"):
    """
    Reads a file stored in MongoDB GridFS and returns its contents in the specified format.

    Parameters:
        database (str): Name of the MongoDB database.
        filename (str): Name of the file to retrieve.
        output_format (str): "auto" (default), "raw", or "base64".

    Returns:
        str or bytes: File contents as text, data URI, raw bytes, or base64 string.
    """
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client[database]
    fs = gridfs.GridFS(db)

    file_metadata = db.fs.files.find_one({"filename": filename})
    if not file_metadata:
        return f"File with filename '{filename}' not found."

    file_data_obj = fs.get(file_metadata['_id'])
    raw_data = file_data_obj.read()

    mime_type, _ = mimetypes.guess_type(filename)

    if output_format == "auto":
        if mime_type:
            if mime_type.startswith("text"):
                try:
                    return raw_data.decode('utf-8')
                except UnicodeDecodeError:
                    return "Error: Failed to decode text file with utf-8 encoding."
            elif mime_type.startswith("image"):
                encoded = base64.b64encode(raw_data).decode('utf-8')
                return f"data:{mime_type};base64,{encoded}"
            else:
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


def retrieve_properties(database, query_params):
    """
    Fetches property files from GridFS whose metadata matches query_params,
    and returns an aggregated list of metadata plus image data URIs.

    Parameters:
        database (str): MongoDB database name.
        query_params (dict): Keys like 'house_type', 'bedrooms'.

    Returns:
        list[dict]: Each dict contains 'house_type', 'bedrooms', and 'data_uri'.
    """
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client[database]
    collection = db['fs.files']

    # Build filter
    query_filter = {}
    if 'house_type' in query_params:
        query_filter['metadata.house_type'] = query_params['house_type']
    if 'bedrooms' in query_params:
        query_filter['metadata.bedrooms'] = query_params['bedrooms']
    if 'amenities' in query_params:
        query_filter['metadata.amenities'] = {'$all': query_params['amenities']}

    documents = collection.find(query_filter)

    results = []
    for doc in documents:
        metadata = doc.get('metadata', {})
        data_uri = output_file_data(database, doc.get('filename'))
        results.append({
        'filename':     doc.get('filename'),
        'house_type':   metadata.get('house_type',   'N/A'),
        'bedrooms':     metadata.get('bedrooms',     'N/A'),
        'amenities':    metadata.get('amenities',    []),
        'address':      metadata.get('address',      'N/A'),
        'city':         metadata.get('city',         'N/A'),
        'state':        metadata.get('state',        'N/A'),
        'zip_code':     metadata.get('zip_code',     'N/A'),
        'owner_name':   metadata.get('owner_name',   'N/A'),
        'owner_address':metadata.get('owner_address','N/A'),
        'owner_email':  metadata.get('owner_email',  'N/A'),
        'data_uri':     data_uri
        })
    return results
