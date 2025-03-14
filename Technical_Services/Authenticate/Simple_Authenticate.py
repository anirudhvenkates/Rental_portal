import pymongo

class SimpleAuthenticate:
    def authenticate_user(database, username, password):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client[database]
        print(username)
        
        # Query the user collection to find the user by username
        user = db.users.find_one({"username": username})

        if user and user["password"] == password:
            return user
            # return user["role"]  # Returning the user's role
        else:
            return None  # Authentication failed
