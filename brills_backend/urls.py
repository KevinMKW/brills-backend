from django.urls import path
from .views import ProfileAPIView, Profile, BillAPIView, Bill

urlpatterns = [
    path('profile/', ProfileAPIView.as_view()),
    path('profile/<uuid:pk>/', Profile.as_view()),
    path('bill/', BillAPIView.as_view()),
    path('bill/<uuid:pk>/', Bill.as_view()),
]
