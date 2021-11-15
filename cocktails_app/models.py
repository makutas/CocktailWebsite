from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    RECIPE_TYPE_CHOICES = [('shaking', 'Shaking'), ('stir', 'Stir'), ('blend', 'Blend')]
    recipe_id = models.AutoField(primary_key=True)
    recipe_author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=30,
                                   unique=True,
                                   error_messages={'unique': 'A recipe with this name already exists!'}
                                   )
    recipe_description = models.CharField(max_length=100, null=True, blank=True)
    recipe_history = models.CharField(max_length=500, null=True, blank=True)
    recipe_type = models.CharField(max_length=20, choices=RECIPE_TYPE_CHOICES)
    date_added = models.DateTimeField(auto_now_add=True)
    recipe_img = models.ImageField(null=True, blank=True)
    tag = models.CharField(max_length=20, null=True)


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=30)
    garnish = models.CharField(max_length=20, null=True)

    class Meta:
        verbose_name_plural = 'ingredients'

    def __str__(self):
        return f"{self.ingredient_name}, {self.ingredient_type}"


class Quantity(models.Model):
    VOLUME_CHOICES = [('ml', 'ml'), ('oz', 'oz'), ('tsp', 'tsp.'), ('tbsp', 'tbsp.'), ]
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    volume = models.IntegerField(null=True, choices=VOLUME_CHOICES)
    pieces = models.IntegerField(null=True)
    dashes = models.IntegerField(null=True)
    spices = models.CharField(max_length=20, null=True)
    # TODO - Think more of these


