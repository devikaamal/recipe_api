from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Recipe(models.Model):
    title=models.CharField(max_length=80)
    cusine=models.CharField(max_length=80)
    meal_type=models.CharField(max_length=80)
    ingredients=models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField(default=0)
    comment=models.TextField()
    rated_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe


