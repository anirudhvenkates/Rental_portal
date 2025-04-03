from flask import Flask, render_template, request, redirect, url_for, flash, session
from Core_Business_Layer.Session import SessionHandler
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

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
        # Recreate the session handler using the stored username and role
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
    operation = request.form.get('operation')  # Retrieve operation from form submission
    operation = operation[3:]
    #print(operation[3:])

    if role and username:
        session_handler = SessionHandler.create_session(username, password)
        if session_handler:
            try:
                print("Session handler created for perform operation:", session_handler)
                result = session_handler.perform_operations(operation)
                print(result)
                flash(result, 'success')
                return render_template('perform_operation.html', result=result)
            except Exception as e:
                flash(str(e), 'danger')
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
    # Redirect to the home page after logout
    return redirect(url_for('home'))

def complex_main():
    app.run(debug=True)