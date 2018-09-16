from django.shortcuts import render
from pos.models import Product, Customer, Order, OrderItem

def invoice_dashboard(request):
    return render(request, 'invoice_dashboard.html')

def customer_invoice(request):
    if request.method == 'POST':
        cid = request.POST.get('customerID', None)
        customer = Customer.objects.get(identity=cid)
        customer_orders = Order.objects.filter(customer=cid).filter(success=True)
        context = {'orders': [order for order in customer_orders],
                'total': sum([int(order.total_price) for order in customer_orders]),
                'customer': customer}
        return render(request, 'customer_invoice_detail.html', context)
    else:
        return render(request, 'customer_invoice.html')
