from django.shortcuts import render

# Create your views here.
# complex_ui/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
import sys
import os

# Add the directory containing 'Core_Business_Layer' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Core_Business_Layer.Session import SessionHandler

from .forms import RegistrationForm, LoginForm

# complex_ui/views.py
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            session_handler = SessionHandler.create_session(username, password)

            if session_handler:
                # Store only serializable data in the session
                session_data = {
                    'name': session_handler.session['name'],
                    'role': session_handler.session['role'],
                    'username': session_handler.session['username'],
                    'operations': session_handler.operations()  # Store the operations directly
                }
                request.session['session_handler'] = session_data  # Store only serializable data
                return redirect('dashboard')  # Redirect to the dashboard
            else:
                return HttpResponse("Authentication failed, please check your credentials.", status=401)
    else:
        form = LoginForm()
    return render(request, 'complex_ui/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            session_handler = SessionHandler.create_session([username, name], password, "Customer")

            if session_handler:
                return redirect('dashboard')  # Redirect to the dashboard
            else:
                return HttpResponse("Failed to create user.")
    else:
        form = RegistrationForm()
    return render(request, 'complex_ui/register.html', {'form': form})

# complex_ui/views.py
def dashboard_view(request):
    # Retrieve session data from the session
    session_data = request.session.get('session_handler')

    if not session_data:
        return redirect('login')  # Redirect to login if session doesn't exist

    # Access session data directly
    user_name = session_data['name']
    user_role = session_data['role']
    operations = session_data['operations']  # Directly access the operations list

    # Pass session-related data and operations to the template
    return render(request, 'complex_ui/dashboard.html', {'name': user_name, 'role': user_role, 'operations': operations})
