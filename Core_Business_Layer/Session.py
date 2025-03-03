from Technical_Services.User_Authentication import authenticate_user
from Core_Business_Layer.Property_Handler import PropertyHandler  # Make sure to import the PropertyHandler class

def create_session(database, username, password):
    # Call User_Authentication to authenticate the user and get session
    session = authenticate_user(database, username, password)
    
    if session:
        # If the user is authenticated, check if the role is 'Staff'
        if session['role'] == 'Staff':
            # Create a PropertyHandler instance and return it along with the session
            return PropertyHandler(session, database)
        else:
            print("Access denied: Only Staff can perform operations.")
            return None  # Role isn't 'Staff'
    else:
        return None  # Authentication failed
