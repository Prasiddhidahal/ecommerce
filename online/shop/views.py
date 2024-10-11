from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Product, Category, Customer
from django.contrib.auth.decorators import login_required
from maintenance_mode.decorators import force_maintenance_mode_off
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from .forms import registerForm, OrderForm
from django.contrib.auth import authenticate, logout, login as auth_login
from .forms import CustomAuthenticationForm
from django.utils import timezone
from .models import register
from django.contrib import messages


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

def registers(request):
    if request.method == 'POST':
        form = registerForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # Save the user from the form
            auth_login(request, user)  # Log in the user
            return redirect('success')  # Redirect to a success page after registration
    else:
        form = registerForm()  # Display the empty registration form

    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            try:
                user = register.objects.get(email=email)
                if user.password == password:
                    auth_login(request, user)
                    user.last_login = timezone.now()
                    user.save()
                    messages.success(request, 'Login successful! Welcome back.')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid password.')
            except register.DoesNotExist:
                messages.error(request, 'Invalid email.')
        else:
            messages.error(request, 'Both email and password are required.')

    return render(request, 'login.html')



def logout(request):
    logout(request)
    return redirect('login')

def success(request):
    return render(request, 'success.html')