from Core_Business_Layer.Session import create_session
from Core_Business_Layer.Property_Handler import perform_operations

def get_user_input():
    # Step 1: Get the username and password from the user
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

def simple_main():
    # Step 2: Get user input (username and password)
    username, password = get_user_input()

    # Step 3: Call Session.py to authenticate the user and create session
    session = create_session('users', username, password)

    if session:
        # Step 4: If the session is valid, check role and perform operations
        if session['role'] == 'Staff':
            print("Welcome",session['name'], "your role is ",session['role'])
            perform_operations(session, 'mydatabase')  # Pass session to Property_Handler
        else:
            print("Access denied: Only Staff can perform operations.")
    else:
        print("Authentication failed. Please check your username and password.")
