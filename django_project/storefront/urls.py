from django.urls import path

from . import views

app_name = 'storefront'

urlpatterns = [
    path('home/', views.view_products, name='home'),
    path('add_product/', views.add_product, name='add_product'),
    path('view_products/', views.view_products, name='view_products')
]