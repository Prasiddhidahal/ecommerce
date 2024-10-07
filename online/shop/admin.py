from django.contrib import admin
# from .models import User
from .models import Product
from .models import Category
from .models import Customer
from .models import Order
# Register your models here.

# admin.site.register(User)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color', 'updated_at')
    # You can add 'color' to fields if you want to make it editable directly
    fields = ['name', 'price', 'description', 'photo', 'color']

admin.site.register(Product, ProductAdmin)

admin.site.register(Category)

admin.site.register(Customer)

admin.site.register(Order)