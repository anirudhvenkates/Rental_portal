from Core_Business_Layer.Session import SessionHandler

def get_user_input_for_registration():
    # Step 1: Get user registration input (username, password, role, name)
    name = input("Enter your full name: ")  # Ask for the user's name
    username = input("Enter username: ")
    password = input("Enter password: ")
    #role = input("Enter role (Customer/Staff): ")
    return username, password, name

def get_user_input_for_login():
    # Step 1: Get username and password for login
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

def simple_main():
    while True:
        print("1. Login")
        print("2. Register User")
        print("Type 'Exit' to quit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            username, password = get_user_input_for_login()
            session_handler = SessionHandler.create_session(username, password)

            if session_handler:
                print("Welcome", session_handler.session['name'], "your role is", session_handler.session['role'])
                
                while True:
                    for op in session_handler.operations():
                        print(op)
                    print("Type Exit to stop")
                        
                    op_choice = input("\nEnter your choice: ")
                    if op_choice == "Exit":
                        print("Terminating the Session")
                        return
                    
                    file_info = input("\nEnter file information (Press Enter for no file input): ")
                    result = session_handler.perform_operations(op_choice, file_info)
                    
                    # In case of a property search, 'result' is an aggregated list.
                    if isinstance(result, list):
                        print("\nProperty Search Results:")
                        for prop in result:
                            print("House Type:", prop.get("house_type"))
                            print("Bedrooms:", prop.get("bedrooms"))
                            print("Image data: (data URI) ", prop.get("data_uri")[:50], "...")  # print a snippet
                            print("-" * 40)
                    else:
                        print("\nOperation result:", result)
            else:
                print("Authentication failed. Please check your username and password.")

        elif choice == "2":
            username, password, name = get_user_input_for_registration()
            session_handler = SessionHandler.create_session([username, name], password, "Customer")
            if session_handler:
                print("User created successfully and session started.")
                print(f"Welcome {session_handler.session['name']}, your role is {session_handler.session['role']}")
                break
            else:
                print("Failed to create user.")
        
        elif choice.lower() == "exit":
            print("Exiting...")
            break
