from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

USER_TYPE_CHOICES = [
    ('farmer', 'Farmer'),
    ('Supplier', 'Supplier'),  
]

class UserManager(BaseUserManager):
    def create_user(self, email, name, phone_number, user_type, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if user_type not in dict(USER_TYPE_CHOICES):
            raise ValueError('Invalid user type')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            phone_number=phone_number,
            type=user_type,
            created_at=timezone.now()
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, phone_number, password):
        user = self.create_user(
            email=email,
            name=name,
            phone_number=phone_number,
            user_type='Supplier',  
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    USER_TYPE_CHOICES = [
    ('farmer', 'Farmer'),
    ('Supplier', 'Supplier'),  
    ]
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  
    
    objects = UserManager()

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['name', 'phone_number']

    def __str__(self):
        return self.email
