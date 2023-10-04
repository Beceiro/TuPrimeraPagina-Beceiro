from django.urls import path
from app_coder import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('customer', views.create_customer, name='customer')
]