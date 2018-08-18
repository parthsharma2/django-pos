from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('billing/', views.billing, name='billing'),
    path('billing/order', views.order, name='order'),
]
