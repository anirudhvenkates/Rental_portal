import hashlib
from pymongo import MongoClient

class UserRegistrationHandler:
    def __init__(self, db_client=None):
        self.db_client = db_client or MongoClient("mongodb://localhost:27017/")
        self.db = self.db_client['users']
        self.collection = self.db['users']

    def hash_password(self, password):
        # A simple hash function (you may want to improve it)
        return hashlib.sha256(password.encode()).hexdigest()

    def generate_user_id(self, role):
        # Generate an ID based on the role (this is just a simple approach)
        user_count = self.collection.count_documents({"role": role})
        # Generate a simple ID like 'S001', 'C001', etc.
        return f"{role[0].upper()}{str(user_count + 1).zfill(3)}"

    def create_user(self, username, password, role, name):
        # Check if the username already exists
        existing_user = self.collection.find_one({"username": username})
        if existing_user:
            return None, "Username already exists."

        # Generate an ID for the user
        user_id = self.generate_user_id(role)

        # Create the new user and insert into MongoDB
        user_data = {
            "name": name,
            "ID": user_id,
            "username": username,
            "password": password,
            "role": role
        }
        result = self.collection.insert_one(user_data)

        if result.inserted_id:
            return user_data, "User created successfully."
        return None, "Failed to create user."
