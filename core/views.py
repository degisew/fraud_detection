import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Transaction
from .form import TransactionForm, CreateUserForm, LoginForm


def detect_fraud(user):
    # daily_transaction_count = Transaction.objects.filter(
    #     user = user,
    #     timestamp__gte = datetime.datetime.now() - datetime.timedelta(days=1)).count()
    # print('#############', daily_transaction_count)
    # if daily_transaction_count > 3:
    #     user.is_fraud = True
    #     user.save()

    daily_transactions = Transaction.objects.filter(
        user = user,
        timestamp__gte = datetime.datetime.now() - datetime.timedelta(days=1))
    print('#############', daily_transactions)
    total_amount = 0
    for dt in daily_transactions:
        total_amount += dt.amount
        if total_amount > 100:
            user.is_fraud = True
            user.save()


@login_required(login_url='/login/')
def create_transaction(request):
    form = TransactionForm(request.POST)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
          # Call the detect_fraud function to check for fraud
        form = TransactionForm()
    detect_fraud(request.user)
    return render(request, 'core/transact_form.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateUserForm()
            return redirect('login')
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
            return redirect('create-transact')
        else:
           return HttpResponse('Authentication Failed!')
        
    return render(request, 'core/login_register_form.html', {'form':form, 'btn_value': 'login'})


def user_logout(request):
    auth.logout(request)
    return redirect('login')