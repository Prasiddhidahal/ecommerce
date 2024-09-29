from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('order/', views.Order, name='order'),
    # path('customer/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('Category/', views.Category, name='Category'),
    path('customer/', views.customer, name='customer'),
    path('Order/', views.Order, name='Order'),

]
