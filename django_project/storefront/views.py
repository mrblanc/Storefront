from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Product

@login_required
def view_products(request):
    allProducts = Product.objects.all()
    context = {'allProducts': allProducts}
    return render(request, 'products/table.html', context)
