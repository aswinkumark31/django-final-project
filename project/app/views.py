from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    pro=models.Products.objects.all()
    return render(request,'index.html',{"pro":pro})

def about(request):
    return render(request,'about.html')

def package(request):
    pro=models.Products.objects.all()
    return render(request,'package.html',{"pro":pro})

def department(request):
    return render(request,'department.html')

def blog(request):
    return render(request,'blog.html')

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    return render(request,'contact.html')

