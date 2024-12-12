from django.contrib import admin
# from .models import User
from .models import Product
from .models import Category
from .models import Customer
from .models import Order
from .models import register
# Register your models here.

# admin.site.register(User)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color', 'updated_at')
    
    fields = ['name', 'price', 'description', 'photo', 'color']

admin.site.register(Product, ProductAdmin)

admin.site.register(Category)

admin.site.register(Customer)

admin.site.register(Order)

admin.site.register(register)

# admin.site.register(login)

# admin.site.register(logout)

