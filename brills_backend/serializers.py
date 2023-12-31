from rest_framework import serializers
from rest_framework.fields import CharField, EmailField, DecimalField
from .models import Profile, Expense

class ProfileSerializer(serializers.ModelSerializer):
    name = CharField(required=True)
    email = EmailField(required=True)
    income = DecimalField(required=True)
    currency = CharField(required=True)
    color = CharField(required=True)

    class Meta:
        model = Profile
        fields = (
            'name',
            'email',
            'income',
            'currency',
            'color'
        )

class ExpenseSerializer(serializers.ModelSerializer):
    name = CharField(source="title", required=True)
    description = CharField(source="description", required=True)
    cost = DecimalField(required=True)

    class Meta:
        model = Expense
        fields = (
            'name',
            'description',
            'cost'
        )