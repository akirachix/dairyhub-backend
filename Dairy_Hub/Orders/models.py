from django.db import models
from farmers.models import Farmer
# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    farmer_id=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    order_date = models.DateField()
    status=models.TextField()
    price = models.DecimalField(decimal_places = 2,max_digits = 6)
    def __str__(self):
      return {self.name.id}

