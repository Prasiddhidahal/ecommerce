# shop/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User  # Importing the User model
from .models import Category, Customer, Product, Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']  # Adjust fields as needed

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'photo', 'color']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'name', 'email', 'phone', 'address', 'country', 'zip_code', 'photo']

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'product', 'quantity', 'price', 'ordered_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'user', 'product', 'quantity', 'added_at']
