from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=30, unique=True, error_messages={'unique': 'A recipe with this name '
                                                                                         'already exists!'})
    recipe_description = models.CharField(max_length=100, null=True)
    recipe_history = models.CharField(max_length=500, null=True)
    # TODO - recipe type (shake, stir, blend)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=30)
    # TODO - This about ingredient type (liquid, fruit, berry)
    garnish = models.CharField(max_length=20, null=True)
    spices = models.CharField(max_length=20, null=True)


class Quantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ml_oz = models.IntegerField(null=True)
    pieces = models.IntegerField(null=True)
    dashes = models.IntegerField(null=True)
    # TODO - Think more of these

