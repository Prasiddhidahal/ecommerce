from django.shortcuts import render,get_object_or_404, redirect
from .models import User, Product, Cart
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
def add_to_cart(request, product_id):
    
    user = request.user  

    
    product = get_object_or_404(Product, id=product_id)

    
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)

 
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()
    
    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1  
        else:
            cart_item.delete()  
        cart_item.save()

    return redirect('cart')

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
