from django.db import models
from cloudinary.models import CloudinaryField

    # account_number= models.IntegerField(default=0)

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100, unique=True)
    address=models.CharField(max_length=100)
    image=CloudinaryField('image',blank=True)
    account_number= models.IntegerField(default=0)



    def __str__(self):
        return self.name

class Account(models.Model):
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    balance=models.FloatField(default=0.0)

    def __str__(self):
        return self.balance

class Cards(models.Model):
    account=models.ForeignKey(Account,on_delete=models.CASCADE) 
    card_number=models.CharField(max_length=16,blank=True, null=True)

    def __str__(self):
        return str(self.card_number)       


