from django.db import models
from django.conf import settings

class Transaction(models.Model):
    user: str = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amout: int = models.PositiveIntegerField()
    timestamp: str = models.DateTimeField(auto_now=True)
    is_fraudlent: bool = models.BooleanField()


    def __str__(self) -> int:
        return self.amout
    
class FraudAlert(models.Model):
    pass