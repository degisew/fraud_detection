from typing import Any
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models.query import QuerySet
from .models import Transaction

    
@admin.register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display = ['user','amount', 'timestamp', 'is_fraudlent']
    list_filter = ['is_fraudlent']