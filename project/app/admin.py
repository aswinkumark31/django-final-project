from django.contrib import admin
from . import models

# Register your models here.

class Product_display(admin.ModelAdmin):
    list_display=['images','price','checkup']

class Gene_display(admin.ModelAdmin):
    list_display=['images','description']

class Image_display(admin.ModelAdmin):
    list_display=['images']
    
admin.site.register(models.Products,Product_display)
admin.site.register(models.Gene,Gene_display)
admin.site.register(models.Gallery,Image_display)
    

