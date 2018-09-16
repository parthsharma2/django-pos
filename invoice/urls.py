from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_dashboard, name='invoice_dashboard'),
    path('customer/', views.customer_invoice, name='customer_invoice')
]
