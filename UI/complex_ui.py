from flask import Flask, render_template, request, redirect, url_for, flash, session
from Core_Business_Layer.Session import SessionHandler
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Define an upload folder for storing temporary files
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session_handler = SessionHandler.create_session(username, password)
        if session_handler:
            print("Session handler created during login:", session_handler)
            session['role'] = session_handler.session['role']
            session['username'] = username  # Store username for session recreation
            session['name'] = session_handler.session['name']
            session['password'] = password
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Authentication failed. Please check your username and password.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        session_handler = SessionHandler.create_session([username, name], password, "Customer")
        if session_handler:
            print("Session handler created during registration:", session_handler)
            session['role'] = session_handler.session['role']
            session['username'] = username  # Store username for session recreation
            session['name'] = session_handler.session['name']
            session['password'] = password
            flash('User created successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Failed to create user.', 'danger')
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    role = session.get('role')
    username = session.get('username')  # Use username for session recreation
    name = session.get('name')
    password = session.get('password')
    if role and username:
        # Recreate the session handler using the stored username and password
        session_handler = SessionHandler.create_session(username, password)
        if session_handler:
            print("Session handler created for dashboard:", session_handler)
            operations = session_handler.operations()
            return render_template('dashboard.html', name=name, role=role, operations=operations)
        else:
            flash('Failed to recreate session handler.', 'danger')
            return redirect(url_for('login'))
    else:
        flash('Please log in to access the dashboard.', 'danger')
        return redirect(url_for('login'))

@app.route('/perform_operation', methods=['POST'])
def perform_operation():
    role = session.get('role')
    username = session.get('username')
    name = session.get('name')
    password = session.get('password')
    
    # Get the selected operation; remove any unwanted prefix if needed.
    operation = request.form.get('operation')
    operation = operation[3:] if operation and len(operation) > 3 else operation

    # Initialize file_info to an empty string.
    file_info = ""
    
    # For "Store a file", check if a file has been uploaded.
    if operation and "store a file" in operation.lower():
        if 'file_input' in request.files:
            file = request.files['file_input']
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                file_info = file_path
                print("File stored at:", file_info)
            else:
                flash("No file selected for upload.", "danger")
                return redirect(url_for('dashboard'))
        else:
            # Fall back to reading file_info from form if file_input is missing.
            file_info = request.form.get('file_info', '')
    
    # For operations that require manual file name input.
    elif operation and ("delete a file" in operation.lower() or "output file data" in operation.lower()):
        file_info = request.form.get('file_info', '')
    
    # For "Retrieve file", no additional file info is required.

    if role and username:
        session_handler = SessionHandler.create_session(username, password)
        if session_handler:
            try:
                print("Session handler created for perform operation:", session_handler)
                result = session_handler.perform_operations(operation, file_info)
                print("Operation result:", result)
                flash(result, 'success')
                return render_template('perform_operation.html', result=result)
            except Exception as e:
                flash(str(e), 'danger')
                return redirect(url_for('dashboard'))
        else:
            flash('Failed to recreate session handler.', 'danger')
            return redirect(url_for('login'))
    else:
        flash('Session handler not found. Please log in again.', 'danger')
        return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    # Clear the user session
    session.pop('role', None)
    session.pop('username', None)
    session.pop('name', None)
    session.pop('password', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

def complex_main():
    app.run(debug=True)

if __name__ == '__main__':
    complex_main()
