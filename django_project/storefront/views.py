from django.shortcuts import render
from .models import Product

def products(request):
    allProducts = Product.objects.all()
    context = {'allProducts': allProducts}
    return render(request, 'products/table.html', context)
