from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from colorfield.fields import ColorField
from django_countries.fields import CountryField

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)
#     address = models.TextField()
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100) 
#     country = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     photo = models.ImageField(upload_to='photo', blank=True, null=True)

#     def __str__(self):
#         return self.name
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='photo', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    COLOR_PALETTE = [
        ("#FFFFFF", "white"),
        ("#000000", "black"),
        ("#FF0000", "red"),
        ("#00FF00", "green"),
        ("#0000FF", "blue"),
        
    ]
    
    
    color = ColorField(samples=COLOR_PALETTE)

    def __str__(self):
        return self.name

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(default=timezone.now)




class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.TextField()
    country = CountryField(multiple=True)  # Confirm this is how you want to define country
    zip_code = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photo', blank=True, null=True)

    def __str__(self):
        return self.name

    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order for {self.product.name} by {self.customer.name}"
    
class register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    last_login = models.DateTimeField(blank=True, null=True)  # Add this field
    photo = models.ImageField(upload_to='photo', blank=True, null=True)

    def __str__(self):
        return self.name

# class login(models.Model):
#     email = models.EmailField()
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.email
    
# class logout(models.Model):
#     email = models.EmailField()
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.email
    
