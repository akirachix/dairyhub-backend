from django.db import models
from users.models import User
# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    farmer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='farmer_orders', limit_choices_to={'type':'farmer'})
    order_date = models.DateField()
    status=models.TextField()
    price = models.DecimalField(decimal_places = 2,max_digits = 6)


    def  order_number(self):
        return self.id

