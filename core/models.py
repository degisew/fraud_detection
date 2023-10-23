
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    is_fraud = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='customuser_set')

    # Define a unique related_name for the user_permissions field
    user_permissions = models.ManyToManyField(
        Permission, related_name='customuser_set'
    )
    def __str__(self):
        return self.username
    
class Transaction(models.Model):
    user: str = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transaction')
    amount: int = models.PositiveIntegerField()
    timestamp: str = models.DateTimeField(auto_now=True)
    

    # def save(self):
    #     if self.amount > 10:
    #         self.is_fraudlent = True
    #     else:
    #         self.is_fraudlent = False
    #     return super().save()
