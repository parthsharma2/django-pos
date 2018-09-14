from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_dash, name='invoice_dashboard')
]
