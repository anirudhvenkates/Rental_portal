from flask import Flask, render_template, request, redirect, url_for, flash, session
from Core_Business_Layer.Session import SessionHandler
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Upload directory
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
            session['role'] = session_handler.session['role']
            session['username'] = username
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
            session['role'] = session_handler.session['role']
            session['username'] = username
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
    username = session.get('username')
    name = session.get('name')
    password = session.get('password')

    if role and username:
        session_handler = SessionHandler.create_session(username, password)
        if session_handler:
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
    operation = request.form.get('operation')
    role = session.get('role')
    username = session.get('username')
    name = session.get('name')
    password = session.get('password')

    if role and username:
        session_handler = SessionHandler.create_session(username, password)
        if not session_handler:
            flash("Failed to recreate session handler.", "danger")
            return redirect(url_for('login'))

        try:
            # Handle staff operation that involves file upload
            if operation.strip().endswith("Store a House Image"):
                file = request.files.get('file_upload')
                house_type = request.form.get('house_type')
                bedrooms = request.form.get('bedrooms')
                if file:
                    from werkzeug.utils import secure_filename
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    file_info = f"file_path {file_path} house_type {house_type} bedrooms {bedrooms}"
                else:
                    flash("File not uploaded properly.", "danger")
                    return redirect(url_for('dashboard'))
            else:
                file_info = request.form.get('file_info', '')

            # Normalize the operation choice if it comes with a prefix, e.g., "1. Search Properties"
            normalized_operation = operation[3:] if len(operation) >= 3 and operation[1:3] == ". " else operation
            result = session_handler.perform_operations(normalized_operation, file_info)

            # For customer search, the EnquiryHandler returns an aggregated list with the keys:
            # "house_type", "bedrooms", and "data_uri"
            if isinstance(result, list):
                return render_template('display_properties.html', properties=result)
            else:
                flash("Operation completed successfully.", "success")
                return render_template('perform_operation.html', result=result)

        except Exception as e:
            flash(str(e), "danger")
            return redirect(url_for('dashboard'))
    else:
        flash("Session expired. Please log in again.", "danger")
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

def complex_main():
    app.run(debug=True)
