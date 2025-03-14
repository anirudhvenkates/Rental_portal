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
                    for i in session_handler.operations():
                        print(i)
                    print("Type Exit to stop")
                        
                    choice = input("\nEnter your choice: ")
                    if choice == "Exit":
                        print("Terminating the Session")
                        return
                    session_handler.perform_operations(choice)
            else:
                print("Authentication failed. Please check your username and password.")

        elif choice == "2":
            username, password, name = get_user_input_for_registration()

            # Pass username, password, and name as a list to create session
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
