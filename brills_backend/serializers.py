from rest_framework import serializers
from rest_framework.fields import CharField, EmailField, DecimalField
from .models import Profile, Bill

class ProfileSerializer(serializers.ModelSerializer):
    name = CharField(required=True)
    email = EmailField(required=True)
    income = DecimalField(max_digits=12, decimal_places=2, required=True)
    currency = CharField(required=True)

    class Meta:
        model = Profile
        fields = (
            'id',
            'name',
            'email',
            'income',
            'currency'
        )

    def create(self, validated_data):
        email = validated_data.pop('email')
        profile_instance = Profile.objects.create(**validated_data)
        profile_instance.email = email
        profile_instance.save()

        return profile_instance

class BillSerializer(serializers.ModelSerializer):
    name = CharField(source="title", required=True)
    description = CharField(required=True)
    cost = DecimalField(max_digits=12, decimal_places=2, required=True)
    color = CharField(required=True)

    class Meta:
        model = Bill
        fields = (
            'id',
            'name',
            'description',
            'cost',
            'color'
        )