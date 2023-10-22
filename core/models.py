from django.db import models
from django.conf import settings

class Transaction(models.Model):
    user: str = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount: int = models.PositiveIntegerField()
    timestamp: str = models.DateTimeField(auto_now=True)
    is_fraudlent: bool = models.BooleanField(default=False)
    

    def save(self):
        if self.amount > 10:
            self.is_fraudlent = True
        else:
            self.is_fraudlent = False
        return super().save()
