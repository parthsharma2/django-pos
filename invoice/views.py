from django.shortcuts import render


def invoice_dash(request):
    return render(request, 'invoice_dashboard.html')
