from django.shortcuts import render,get_object_or_404, redirect
from .models import User, Product, Category
from django.contrib.auth.decorators import login_required

def index(request):
    users = User.objects.all()  
    return render(request, 'index.html', {'users': users})  

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    products = Product.objects.all()  
    return render(request, 'products.html', {'products': products})  

def home(request):
    return render(request, 'home.html')  

@login_required
def Category(request):
    Category_items = Category.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in Category_items)

    return render(request, 'category.html', {'Category_items': Category_items, 'total_price': total_price})

@login_required
def Customer(request):
    return render(request, 'customer.html')

@login_required
def Order(request):
    return render(request, 'order.html')
