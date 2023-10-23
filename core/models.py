from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.conf import settings




class CustomUser(AbstractUser):
    is_fraud = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Transaction(models.Model):
    user: str = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='transaction')
    amount: int = models.PositiveIntegerField()
    timestamp: str = models.DateTimeField(auto_now=True)
    # is_fraudlent: bool = models.BooleanField(default=False)
    

    # def save(self):
    #     if self.amount > 10:
    #         self.is_fraudlent = True
    #     else:
    #         self.is_fraudlent = False
    #     return super().save()
