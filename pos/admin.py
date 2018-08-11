from django.contrib import admin
from .models import Product, Customer, Order, OrderItem


admin.site.site_header = 'POS Administration'
admin.site.site_title = 'POS Administration'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('identity', 'name', 'balance')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_price', 'success', 'timestamp')
    list_filter = ('success', 'timestamp')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'timestamp', 'product')
    list_filter = ('order', 'timestamp')


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
