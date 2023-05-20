from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    is_created = models.DateTimeField(auto_now=True)
    is_updated = models.DateTimeField(auto_now=True)

class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)

class Product(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='app/img/logo')
    images = models.ImageField(upload_to='app/img/images')
    text = models.CharField(max_length=500)
    link = models.URLField(max_length=500)
    address = models.CharField(max_length=200)
    contact = models.IntegerField()
    product_card = models.ImageField(upload_to='app/img/products')

class contact(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    product = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now=True)
