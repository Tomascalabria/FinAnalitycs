from django.db import models
from .Encrypt import EncryptedPasswordField

class Credentials(models.Model):
    user_id = models.CharField(max_length=255)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, default=0)
    username = models.CharField(max_length=255)
    password = EncryptedPasswordField(max_length=255)


class Balance(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, default=0)
    user_id = models.CharField(max_length=255)
    balance_ars = models.DecimalField(max_digits=10, decimal_places=2)
    balance_usd = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)
    

class Holding(models.Model):
    ticker = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    weight = models.FloatField(default=0)  # Add the weight column
    user_id = models.CharField(max_length=255)
    variation = models.FloatField(null=True)
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE, default=0)


class BuySellMovement(models.Model):
    ticker = models.CharField(max_length=50)
    operation = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    total_movement = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, default=0)
    user_id = models.CharField(max_length=255)

class DepositExtractionMovement(models.Model):
    ticker = models.CharField(max_length=50)
    operation = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    total_movement = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, default=0)
    user_id = models.CharField(max_length=255)

class Company(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    logo = models.URLField()
    about = models.TextField()


