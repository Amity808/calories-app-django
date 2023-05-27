from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Customer, UserFoodItem, Category, FoodItem
from .forms import FoodItemForm, UserFoodItemForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group
from .filers import *

# Create your views here.


def home(request):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()[:5]
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()
