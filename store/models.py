from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Restaurant(models.Model):
    name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    far=models.IntegerField(default=0,null=True)
    description=models.TextField(null=True)
    rating=models.FloatField(default=0.0,null=True)
    total_rating = models.IntegerField(default=0,null=True)
    total_users = models.IntegerField(default=0,null=True)
    class Meta:
        ordering=('name',)
    def __str__(self):
        return f'{self.name} by {self.location}'

class Food(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    mrp=models.PositiveIntegerField()
    sale=models.IntegerField(null=True,default=0)
    category=models.CharField(max_length=50,default='Main Course')
    def __str__(self):
        return(self.name)



class FoodOrder(models.Model):
    food=models.ForeignKey(Food,on_delete=models.CASCADE)
    order_time=models.DateField(null=True)
    customer=models.ForeignKey(User,related_name='customer',null=True,on_delete=models.SET_NULL)
    total_amt=models.IntegerField(default=0,null=True)
    def __str__(self):
        return(self.food.name)

class PastOrders(models.Model):
    foodlist=models.TextField(null=True)
    customer2=models.ForeignKey(User,related_name='customer2',null=True,on_delete=models.SET_NULL)
    cost=models.IntegerField(default=0,null=True)
    restname=models.CharField(max_length=50,null=True)
    order_date=models.DateField(null=True)
    def __str__(self):
        return(self.foodlist)



        



            
            
                        



