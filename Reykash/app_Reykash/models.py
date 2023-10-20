from django.db import models

# Create your models here.
class Post(models.Model):
    text= models.CharField(max_length=30)
    create_att = models.DateField()
    
class Dg(models.Model):
    name= models.CharField(max_length=30)
    surnmae = models.CharField(max_length=30)
    dateofbirth=models.CharField(max_length=100)
    gmail=models.CharField(max_length=100)
    age=models.Integer(max_length=100)