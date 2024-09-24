from django.shortcuts import render
from .models import User, Product

def index(request):
    users = User.objects.all()  # Fetch all users for the home page
    return render(request, 'index.html', {'users': users})  # Pass users to the template

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    products = Product.objects.all()  # Fetch all products for the products page
    return render(request, 'products.html', {'products': products})  # Pass products to the template

def home(request):
    return render(request, 'home.html')  # Optionally keep this for a dedicated home page if needed
