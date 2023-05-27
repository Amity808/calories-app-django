from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# This will take care of all access privileges so that
# the customer and the admin cannot access each other’s
# data. Also, it will make sure that the logged-in user
# can’t go to the login/register page, unauthorized users
# can’t access any page except login and registration page.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=100, null=True)
    date_posted = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    options = (
        ('breakfast','Breakfast'),
        ('lunch','Lunch'),
        ('dinner', 'Dinner'),
        ('snacks', 'Snacks'),
        ('fruits', 'fruits'),
    )

    name = models.CharField(max_length=40,choices=options)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    carbohydrate = models.DecimalField(max_length=10, decimal_places=2, default=0, max_digits=20)
    fats = models.DecimalField(max_length=10, decimal_places=2, default=0, max_digits=20)
    protein = models.DecimalField(max_length=10, decimal_places=2, default=0, max_digits=20)
    calories = models.DecimalField(max_length=10, decimal_places=2, default=0, max_digits=20)
    quantity = models.DecimalField(max_length=10, decimal_places=2, default=0, max_digits=20)

    def __str__(self):
        return self.name


# for Use page
class UserFoodItem(models.Model):
    customer = models.ManyToManyField(Customer, blank=True)
    fooditem = models.ManyToManyField(FoodItem)
