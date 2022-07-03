from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product
from .models import User

admin.site.register(Product)
admin.site.register(User, UserAdmin)
