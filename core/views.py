from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .form import TransactionForm, CreateUserForm, LoginForm

@login_required(login_url='/login/')
def create_transaction(request):
    form = TransactionForm()
    form = TransactionForm(request.POST)
    if form.is_valid():
        form.instance.user = request.user
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

    return render(request, 'core/login_register_form.html', {'form': form, 'btn_value': 'Register'})


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('create-transact')  # Redirect to user's profile page
        else:
           return HttpResponse('Authentication Failed!')
        
    return render(request, 'core/login_register_form.html', {'form':form, 'btn_value': 'login'})


def user_logout(request):
    auth.logout(request)
    return redirect('login')  # Redirect to the login page after logout