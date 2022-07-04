from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from datetime import datetime

from .models import Product
from .forms import AddProduct

@login_required
def add_product(request):
    if request.method == "POST":
        form = AddProduct(request.POST)
        if form.is_valid():
            product = Product()
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.date_added = datetime.now()
            product.save()
            return redirect('storefront:view_products')
    else:
        form = AddProduct()
    context = {'form': form}
    return render(request, 'products/add.html', context)

@login_required
def view_products(request):
    allProducts = Product.objects.all()
    context = {'allProducts': allProducts}
    return render(request, 'products/table.html', context)
