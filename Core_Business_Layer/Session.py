from Core_Business_Layer.Enquiry_Handler import EnquiryHandler
from Core_Business_Layer.Property_Handler import PropertyHandler
from Technical_Services.Authenticate.UserRegistrationHandler import UserRegistrationHandler
from Technical_Services.Authenticate.Authenticate_Handler import AuthenticateHandler
from Technical_Services.Logging.Logger_Service import LoggingService

class SessionHandler:
    @staticmethod
    def create_session(user_info, password, role=None):
        # Extract username and name from the user_info list
        username = user_info
        logger = LoggingService(username)
        # Check if role is None (if it's for login)
        if role is None:
            # Handle authentication
            session = AuthenticateHandler.authenticate("simple", username, password)

            if session:
                # Return the appropriate handler based on the role
                session['logger'] = logger
                if session['role'] == 'Staff':
                    return PropertyHandler(session)
                elif session['role'] == 'Customer':
                    return EnquiryHandler(session)
                else:
                    print("Access denied: Invalid role.")
                    return None
            else:
                return None
        
        # If role is provided (during registration), handle user creation
        if role:
            # Create a new user (for customers)
            registration_handler = UserRegistrationHandler()
            user_data, message = registration_handler.create_user(username[0], password, role, username[1])

            if user_data:
                print(message)
                # Return the corresponding handler for the new user
                if role == 'Staff':
                    return PropertyHandler(user_data)  # Staff user handler
                elif role == 'Customer':
                    return EnquiryHandler(user_data)  # Customer user handler
                else:
                    print("Invalid role provided.")
                    return None
            else:
                print(message)  # Print the error message from registration
                return None
