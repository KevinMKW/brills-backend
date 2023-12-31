from django.urls import path
from .views import UserProfileList, ExpenseList

urlpatterns = [
    path('/user-profiles/', UserProfileList.as_view(), name='user-profile-list'),
    path('/expenses/', ExpenseList.as_view(), name='expense-list'),
]
