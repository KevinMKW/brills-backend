from django.contrib import admin
from .models import Profile, Bill


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'income', 'currency')

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'cost', 'color')