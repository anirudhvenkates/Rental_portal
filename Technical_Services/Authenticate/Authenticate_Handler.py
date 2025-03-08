import pymongo
from Technical_Services.Authenticate.Simple_Authenticate import SimpleAuthenticate
from Technical_Services.Authenticate.Third_Party_Authenticate import ThirdPartyAuthenticate

class AuthenticateHandler:
    
    @staticmethod
    def authenticate(choice, username, password):
        database = "users"
        if choice == "simple":
            return SimpleAuthenticate.authenticate_user(database, username, password)
        elif choice == "third":
            return ThirdPartyAuthenticate.authenticate_user(database, username, password)
        else:
            raise ValueError(f"Unsupported authentication method: {choice}")
            