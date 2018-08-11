from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Customer(models.Model):
    identity = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '{0} ({1})'.format(self.identity, self.name)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    success = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)


class Order_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
