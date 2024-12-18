from django import forms
# from .models import User
from .models import Product
from .models import Category, Customer, Order,register
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import re

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
#         labels = {
#             'name': 'Full Name',
#             'email': 'Email Address',
#             'password': 'Password',
#             'phone': 'Phone Number',
#             'address': 'Address',
#             'city': 'City',
#             'state': 'State',
#             'country': 'Country',
#             'zip_code': 'Zip Code',
#             'photo': 'Photo',
#         }
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'address': forms.Textarea(attrs={'class': 'form-control'}),
#             'city': forms.TextInput(attrs={'class': 'form-control'}),
#             'state': forms.TextInput(attrs={'class': 'form-control'}),
#             'country': forms.TextInput(attrs={'class': 'form-control'}),
#             'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
#             'photo': forms.ImageInput(attrs={'class': 'form-control'}),
#         }




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Product Name',
            'price': 'Product Price',
            'description': 'Product Description',
            'photo': 'Product Photo',
            'color': 'Product Color',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
        }



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'product': 'Product',
            'quantity': 'Quantity',
        }
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'user': 'User', 
            'name': 'customer Name',
            'email': 'customer Email',  
            'phone': 'customer Phone',
            'address': 'customer Address',
            
            'state': 'customer State',
            'country': 'customer Country',

            'zip_code': 'customer Zip Code',
            'photo': 'customer Photo',

        }
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'quantity', 'price']  # Exclude price if you want to calculate it in the view
        labels = {
            'customer': 'Customer',
            'product': 'Product',
            'quantity': 'Quantity',
            'price': 'Price',
        }
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
class registerForm(forms.ModelForm):
    class Meta:
        model = register
        fields = '__all__'
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'password': 'Password',
            'phone': 'Phone Number',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'country': 'Country',
            'zip_code': 'Zip Code',
            'photo': 'Photo',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),  # Updated to ClearableFileInput
        }

class loginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}) )

    class Meta:
        model = register
        fields = ['email', 'password']

class logoutForm(forms.Form):
    pass

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')