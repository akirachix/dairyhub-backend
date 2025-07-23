
from django.db import models

from users.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    Supplier=models.ForeignKey(User,on_delete=models.CASCADE,related_name='supplier_orders',limit_choices_to={'type':'Supplier'})
    product_image_url = models.URLField(max_length=500)
    
    def __str__(self):
        return self.name

