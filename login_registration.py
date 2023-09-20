from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    """
    Handle user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    """
    Handle user login.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid username or password')
    return render(request, 'registration/login.html')


def user_logout(request):
    """
    Handle user logout.
    """
    logout(request)
    return redirect('login')
