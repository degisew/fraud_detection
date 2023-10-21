from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .form import TransactionForm, CreateUserForm, LoginForm


def create_transaction(request):
    form = TransactionForm()
    form = TransactionForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'core/transact_form.html', {'form': form})


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page
    else:
        form = CreateUserForm()

    return render(request, 'core/register.html', {'form': form})


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirect to user's profile page
        else:
           return HttpResponse('Authentication Failed!')
        
    return render(request, 'core/login.html', {'form':form})


def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout