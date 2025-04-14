# Technical_Services/Property_Retriever.py
import pymongo
from Technical_Services.File_Operations.FileHandler import FileHandler

def retrieve_properties(database, query_params):
    """
    Connects to MongoDB and retrieves property listings from GridFS's "fs.files" collection
    that match the query_params (in the metadata). For each matching document, it calls the 
    output_data function to get the encoded image as a data URI. Then it returns an aggregated 
    result containing only the property metadata and the encoded image data.

    Parameters:
        database (str): MongoDB database name.
        query_params (dict): Should contain keys like 'house_type' and 'bedrooms'.

    Returns:
        list: A list of dictionaries with keys 'house_type', 'bedrooms', and 'data_uri'.
    """
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client[database]
    
    # Querying GridFS files collection
    collection = db["fs.files"]

    query_filter = {}
    if "house_type" in query_params:
        query_filter["metadata.house_type"] = query_params["house_type"]
    if "bedrooms" in query_params:
        query_filter["metadata.bedrooms"] = query_params["bedrooms"]

    documents = list(collection.find(query_filter))
    
    # Create a FileHandler instance to get file data (data URIs)
    file_handler = FileHandler(database)
    aggregated_results = []
    
    for doc in documents:
        metadata = doc.get("metadata", {})
        # Get the encoded image data from output_data without including the filename in the result.
        data_uri = file_handler.output_data(doc.get("filename"))
        aggregated_results.append({
            "house_type": metadata.get("house_type", "N/A"),
            "bedrooms": metadata.get("bedrooms", "N/A"),
            "data_uri": data_uri
        })
        
    return aggregated_results
