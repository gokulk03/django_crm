from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200,null = True)
    phone = models.IntegerField(max_length=11,null = True)
    email = models.CharField(max_length=200,null= True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    CATEGORY = (('Indoor','Indoor'),('Out Door','Out Door'),)
    name = models.CharField(max_length=100,null = True)
    price = models.FloatField(max_length=100 ,null = True)
    category = models.CharField(max_length=100,null =True,choices = CATEGORY)
    description = models.CharField(max_length=200,null = True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (('Pending','Pending'),('Out for delivery','Out for delivery'),('Delivered','Delivered'),)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    cutomer = models.ForeignKey(Customer,null = True,on_delete=models.SET_NULL)
    status = models.CharField(max_length = 200,null = True,choices=STATUS)
    
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    

