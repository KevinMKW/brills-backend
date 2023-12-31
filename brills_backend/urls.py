from django.urls import path
from .views import ProfileAPIView, BillAPIView

urlpatterns = [
    path('profile/', ProfileAPIView.as_view()),
    path('bill/', BillAPIView.as_view()),
]
