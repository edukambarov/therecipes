import datetime

from django.core.validators import MinValueValidator
from django.db import models
from users.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class Ingredient(models.Model):
    MEASURES = [
        ('шт.', 'шт.'),
        ('гр.', 'гр.'),
        ('ст.л.', 'ст.л.'),
        ('чай.л.', 'чай.л.'),
        ('мл.', 'мл.'),
    ]
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    measure = models.CharField(max_length=6, choices=MEASURES, default='гр.')


    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps_cooking = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    time_for_cooking = models.IntegerField(default=10)
    photo = models.ImageField(upload_to='images', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def get_m2m_date(self):
        return {'categories': self.categories, 'ingredients': self.ingredients}

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


