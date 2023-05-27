from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Customer, FoodItem, UserFoodItem
from django.contrib.auth.forms import UserCreationForm


class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = '__all__'


class UserFoodItemForm(ModelForm):
    class Meta:
        model = UserFoodItem
        fields = '__all__'


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password1']
