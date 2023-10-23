
from django.contrib import admin
# from django.contrib.admin import ModelAdmin
# from django.db.models.query import QuerySet
# from .models import Transaction
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CustomUser, Transaction

def mark_as_fraud(modeladmin, request, queryset):
    for user in queryset:
        user.is_fraud = True
        user.save()

mark_as_fraud.short_description = "Mark selected users as potential fraud"

class CustomUserAdmin(UserAdmin):
    actions = [mark_as_fraud]
    list_display = ['first_name', 'last_name', 'email', 'is_fraud']
    list_filter = ['is_fraud']


admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.unregister(User)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'timestamp']