from django.urls import path
from .views import ProfileAPIView, ExpenseAPIView

urlpatterns = [
    path('profile/', ProfileAPIView.as_view()),
    path('expenses/', ExpenseAPIView.as_view()),
]
