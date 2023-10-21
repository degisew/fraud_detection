from django.shortcuts import render
from .form import TransactionForm

form = TransactionForm()

def create_transaction(request):
    context = {'forms': form}
    return render(request, 'core/transact_form.html', context)