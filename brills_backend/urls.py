from django.urls import path
from .views import UserProfileList, ExpenseList

urlpatterns = [
    path('api/user-profiles/', UserProfileList.as_view(), name='user-profile-list'),
    path('api/expenses/', ExpenseList.as_view(), name='expense-list'),
]
