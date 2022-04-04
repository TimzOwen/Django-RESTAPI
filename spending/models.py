from django.db import models


# Create your models here.

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=200)
