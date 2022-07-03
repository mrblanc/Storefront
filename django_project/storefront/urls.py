from django.urls import path

from . import views

app_name = 'storefront'

urlpatterns = [
    path('home/', views.view_products, name='home'),
    path("view_products/", views.view_products, name="view_products")
]