from django.http import HttpResponse
from django.shortcuts import render
from .models import Transaction
from .form import TransactionForm


def create_transaction(request):
    form = TransactionForm()
    form = TransactionForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'core/transact_form.html', {'forms': form})

def detect_fraud(request):
    transactions = Transaction.objects.all()
    for transaction in transactions:
        if transaction.amount >10:
            transaction.is_fraudlent = True
    return HttpResponse('Detection Complete!')