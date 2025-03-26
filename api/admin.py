from django.contrib import admin
from api.models import *


# Register your models here.
@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id','name','price','quantity','discount','tax','status', 'created_at', 'updated_at')
   