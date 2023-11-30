from django.db import models

# Create your models here.

class Products(models.Model):
    images=models.CharField(max_length=3000)
    price=models.IntegerField()
    checkup=models.CharField(max_length=50)

class Gene(models.Model):
    images=models.CharField(max_length=3000)
    description=models.CharField(max_length=300)

class Gallery(models.Model):
    images=models.CharField(max_length=3000)
    