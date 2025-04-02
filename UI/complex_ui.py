from flask import Flask, render_template, request, redirect, url_for, flash
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
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard', role=session_handler.session['role']))
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
            flash('User created successfully!', 'success')
            return redirect(url_for('dashboard', role=session_handler.session['role']))
        else:
            flash('Failed to create user.', 'danger')
    return render_template('register.html')

@app.route('/dashboard/<role>')
def dashboard(role):
    return render_template('dashboard.html', role=role)

def complex_main():
    app.run(debug=True)