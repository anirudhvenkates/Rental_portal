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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            session_handler = SessionHandler.create_session(username, password)

            if session_handler:
                # Store session handler object or relevant user data in Django's session
                request.session['session_handler'] = {
                    'name': session_handler.session['name'],
                    'role': session_handler.session['role']
                }
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

def dashboard_view(request):
    # Here, you would retrieve user session data
    session_handler = request.session.get('session_handler')

    if not session_handler:
        return redirect('login')  # Redirect to login if session doesn't exist

    user_name = session_handler['name']
    user_role = session_handler['role']
    
    # Pass session-related data to the template
    return render(request, 'complex_ui/dashboard.html', {'name': user_name, 'role': user_role})
