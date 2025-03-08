from Core_Business_Layer.Enquiry_Handler import EnquiryHandler
from Core_Business_Layer.Property_Handler import PropertyHandler
from Technical_Services.Authenticate.Authenticate_Handler import AuthenticateHandler

class SessionHandler:
    @staticmethod
    def create_session(username, password):
        #database = "users"
        session = AuthenticateHandler.authenticate("simple", username, password)

        if session:
            if session['role'] == 'Staff':
                # Staff can access full file operations
                return PropertyHandler(session)
            elif session['role'] == 'Customer':
                # Customer can only retrieve files
                return EnquiryHandler(session)
            else:
                print("Access denied: Invalid role.")
                return None
        else:
            return None
