from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('bills', views.billList, name="bills"),
    path('bill-details/<str:pk>', views.billDetails, name="bills-details"),
    path('bill-create', views.billCreate, name="bills-create"),
    path('bill-update/<str:pk>', views.billUpdate, name="bills-update"),
    path('bill-delete/<str:pk>', views.billDelete, name="bills-delete"),
]
