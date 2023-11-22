from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    pro=models.Products.objects.all()
    return render(request,'index.html',{"pro":pro})


