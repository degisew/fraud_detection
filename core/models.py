from django.db import models
from django.conf import settings

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amout = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now=True)
    is_fraudlent = models.BooleanField()

class FraudAlert(models.Model):
    pass