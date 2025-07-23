from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 'name', 'phone_number', 'type', 'email',
        'created_at', 
    )
    list_filter = ('type', 'created_at')
    search_fields = ('name', 'phone_number')
admin.site.register(User, UserAdmin)