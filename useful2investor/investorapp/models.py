from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

class Email(models.Model):
    address = models.EmailField(default='example@example.com')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Asset(models.Model):
    name = models.CharField(max_length=100)
    verification_time = models.PositiveIntegerField()
    superior_limit = models.DecimalField(max_digits=10, decimal_places=2)
    inferior_limit = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)