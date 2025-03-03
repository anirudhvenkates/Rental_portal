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
    property_handler = SessionHandler.create_session('users', username, password)

    if property_handler:
        print("Welcome", property_handler.session['name'], "your role is", property_handler.session['role'])
        
        while True:
            for i in property_handler.operations():
                print(i)
            print("Type Exit to stop")
                
            choice = input("\nEnter your choice: ")
            if choice == "Exit":
                print("Terminating the Session")
                return
            property_handler.perform_operations(choice)
    else:
        print("Authentication failed. Please check your username and password.")
