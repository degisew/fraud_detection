from django.http import HttpResponse
from django.shortcuts import render
from .form import TransactionForm


def create_transaction(request):
    form = TransactionForm()
    form = TransactionForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'core/transact_form.html', {'forms': form})
