from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import TimeStampedModel, ActivatorModel, TitleDescriptionModel


class Profile(TimeStampedModel, ActivatorModel, Model):
    class Meta: 
        verbose_name_plural = "Profiles"

    name = models.CharField(max_length=255)
    email = models.EmailField()
    income = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    color = models.CharField(max_length=7, null=True, blank=True, help_text="Hex color code, e.g., #RRGGBB")


    def __str__(self):
        return f"{self.name} - {self.currency}"

class Expense(TitleDescriptionModel, Model):
    class Meta:
        verbose_name_plural = "Expences"

    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} - {self.cost}"