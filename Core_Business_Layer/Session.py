from Technical_Services.User_Authentication import authenticate_user

def create_session(database, username, password):
    # Call User_Authentication to authenticate the user and get session
    session = authenticate_user(database, username, password)
    
    if session:
        return session  # Return session to UI Layer
    else:
        return None  # Authentication failed
