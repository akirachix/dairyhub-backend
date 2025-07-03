from django.db import models

# Create your models here.
from django.db import models
USER_TYPE_CHOICES = [
    ('farmer', 'Farmer'),
    ('Supplier', 'Supplier'),
]
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length = 100)
    password_hash = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
   
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"