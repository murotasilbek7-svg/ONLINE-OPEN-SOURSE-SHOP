from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
   return print("Product List View Accessed")