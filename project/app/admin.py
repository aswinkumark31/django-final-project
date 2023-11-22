from django.contrib import admin
from . import models

# Register your models here.

class Product_display(admin.ModelAdmin):
    list_display=['images','price','checkup']
    
admin.site.register(models.Products,Product_display)
    

