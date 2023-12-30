from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=255)
    income = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(maxx_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.cost}"