from django.contrib import admin

# Register your models here.
from products.models import Product, Category, Review

admin.site.register([Product, Category, Review])
