from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('bills/', views.billList, name="bills"),
    path('bill-details/<str:pk>/', views.billDetails, name="bill-details"),
    path('bill-create/', views.billCreate, name="bill-create"),
    path('bill-update/<str:pk>/', views.billUpdate, name="bill-update"),
    path('bill-delete/<str:pk>/', views.billDelete, name="bill-delete"),

    path('profiles/', views.profileList, name="profiles"),
    path('profile-details/<str:pk>/', views.profileDetails, name="profile-details"),
    path('profile-create/', views.profileCreate, name="profile-create"),
    path('profile-update/<str:pk>/', views.profileUpdate, name="profile-update"),
    path('profile-delete/<str:pk>/', views.profileDelete, name="profile-delete"),
    path('send-magic-link/', views.send_magic_link_view, name='send_magic_link_view'),
]
