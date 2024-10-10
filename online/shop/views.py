from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Product, Category, Customer
from django.contrib.auth.decorators import login_required
from maintenance_mode.decorators import force_maintenance_mode_off
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import registerForm, OrderForm
from django.contrib.auth import authenticate, logout, login as auth_login
from .forms import CustomAuthenticationForm

def index(request):
    users = User.objects.all()  
    return render(request, 'index.html', {'users': users})  

@force_maintenance_mode_off
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
@force_maintenance_mode_off
def customer(request):
    customer = Customer.objects.all()  
    return render(request, 'customer.html', {'customer': customer})  
@force_maintenance_mode_off
@login_required
def Order(request):
    customers = Customer.objects.all()
    products = Product.objects.all()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Create order instance without saving it yet
            order = form.save(commit=False)
            # Calculate price based on selected product and quantity
            order.price = order.product.price * order.quantity
            # Save the order instance to the database
            order.save()
            print("Order saved successfully!")  # Debugging statement
            return redirect('home')  # Redirect to success page
        else:
            print("Form is invalid:", form.errors)  # Debugging statement
    else:
        form = OrderForm()

    context = {
        'form': form,
        'customers': customers,
        'products': products,
    }
    return render(request, 'order.html', context)

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST, request.FILES)
        if form.is_valid():
            
            user = form.save()  
            
            auth_login(request, user)  
            return redirect('success')  
    else:
        form = registerForm()
    
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)  # Use your custom form
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        initial_data = {'username': '', 'password': ''}
        form = CustomAuthenticationForm(initial=initial_data)

    return render(request, 'login.html', {'form': form})


def logout(request):
    logout(request)
    return redirect('login')

def success(request):
    return render(request, 'success.html')