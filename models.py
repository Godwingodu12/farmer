from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Registration(models.Model):
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Contact=models.BigIntegerField()
    Email=models.EmailField()
    Aadhar=models.ImageField()
    password=models.CharField(max_length=20)
    status=models.IntegerField(null=True)
    proof=models.ImageField(null=True)

class Public(models.Model):
    Name=models.CharField(max_length=20)
    Contact=models.BigIntegerField()
    Email=models.EmailField()
    password=models.CharField(max_length=20)
    status=models.IntegerField(null=True)

class Investors(models.Model):
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Contact=models.BigIntegerField()
    Email=models.EmailField()
    license=models.ImageField()
    prof=models.ImageField()
    password=models.CharField(max_length=20)
    status=models.IntegerField(null=True)


class Expert(models.Model):
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Contact=models.BigIntegerField()
    Email=models.EmailField()
    Aadhar=models.ImageField()
    password=models.CharField(max_length=20)
    status=models.IntegerField(null=True)
    proof=models.ImageField(null=True)

class CustomUser(AbstractUser):
    usertype=models.CharField(max_length=15,null=True)

    
class Category(models.Model):
    cat=models.CharField(max_length=20)
    type=models.CharField(max_length=20)


class Specbook(models.Model):
    did=models.ForeignKey(Expert,on_delete=models.CASCADE)
    
    status=models.CharField(max_length=20)
    user=models.ForeignKey(Registration,on_delete=models.CASCADE)
    info=models.CharField(max_length=50,null=True)
    

class Supplier(models.Model):
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Contact=models.BigIntegerField()
    Email=models.EmailField()
    Aadhar=models.ImageField()
    password=models.CharField(max_length=20)
    status=models.IntegerField(null=True)
    proof=models.ImageField(null=True)

class Products(models.Model):
    Name=models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.ImageField()
    quantity=models.IntegerField()
    desc=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

class Yield(models.Model):
    Name=models.CharField(max_length=20)
    price=models.BigIntegerField()
    image=models.ImageField()
    quantity=models.BigIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    fid=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)


class Plans(models.Model):
    iid=models.ForeignKey(Investors,on_delete=models.CASCADE)
    Name=models.CharField(max_length=20)
    Amount=models.BigIntegerField()
    Time=models.IntegerField()
    rate=models.FloatField()
    emi=models.BigIntegerField()
    image=models.ImageField(null=True)

class Payment(models.Model):
    sender=models.EmailField(null=True)
    receiver=models.EmailField(null=True)
    date=models.DateField()
    amt=models.FloatField()

class ProdBook(models.Model):
    pid=models.ForeignKey(Products,on_delete=models.CASCADE)
    amt=models.FloatField()
    qty=models.FloatField()
    user=models.ForeignKey(Registration,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,null=True)
    date=models.DateField()






class Complaint(models.Model):
    title = models.CharField(max_length=20)
    pid = models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)
    complaint = models.CharField(max_length=200)
    cat = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)


class Chat(models.Model):
    sender=models.CharField(max_length=20)
    receiver=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    message=models.CharField(max_length=400) 