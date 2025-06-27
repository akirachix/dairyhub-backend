from django.db import models

# from Orders.models import Order

# from suppliers.models import Supplier

from products.models import Product


# Create your models here.
class OrderItem(models.Model):
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.id} {self.quantity}"