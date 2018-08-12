from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Customer, Order, OrderItem


def dashboard(request):
    return render(request, 'dashboard.html')

def billing(request):
    if request.method == 'GET':
        return render(request, 'billing.html')
    else:
        cid = request.POST.get('customerID', None)
        customer = Customer.objects.filter(pk=cid)
        context = {'name' : customer[0].name, 'balance' : customer[0].balance}
        return render(request, 'billing_details.html', context)
