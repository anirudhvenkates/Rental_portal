from Core_Business_Layer.Session import SessionHandler

def get_user_input():
    # Step 1: Get the username and password from the user
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

def simple_main():
    # Step 2: Get user input (username and password)
    username, password = get_user_input()

    # Step 3: Call Session.py to authenticate the user and create session
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
