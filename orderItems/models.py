from django.db import models


from users.models import User

from products.models import Product


# Create your models here.
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Supplier=models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'type':'Supplier'})
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.id} {self.quantity}"