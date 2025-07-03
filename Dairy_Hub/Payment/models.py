from django.db import models
# from orderItems.models import OrderItem

class Payment(models.Model):
    # order_item_id = models.ForeignKey(OrderItems, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=100,decimal_places=2)
    payment_method = models.CharField(max_length=50)
    date_paid = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):

        return f"Payment of {self.amount_paid} for order {self.date_paid}"

# Create your models here.


