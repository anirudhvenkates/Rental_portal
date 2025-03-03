import pymongo
from Technical_Services.Authenticate.Simple_Authenticate import SimpleAuthenticate
from Technical_Services.Authenticate.Third_Party_Authenticate import ThirdPartyAuthenticate

class AuthenticateHandler:
    def authenticate(choice, database, username, password):
        if choice == "simple":
            return SimpleAuthenticate.authenticate_user(database, username, password)
        else:
            raise ValueError(f"Unsupported authentication method: {choice}")