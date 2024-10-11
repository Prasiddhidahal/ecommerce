from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.products, name='products'),
    path('Category/', views.Category, name='Category'),
    path('customer/', views.customer, name='customer'),
    path('Order/', views.Order, name='Order'),
    path('registers/', views.registers, name='registers'),
    path('success/', views.success, name='success'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
