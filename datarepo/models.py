from django.db import models

# Create your models here.
class Furniture(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    price=models.IntegerField()
    color=models.CharField(max_length=255,null=True,blank=True)
    brand=models.CharField(max_length=255,null=True,blank=True)
    quantity=models.IntegerField()

class Details(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    discription=models.TextField()