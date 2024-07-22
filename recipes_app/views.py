import datetime
import os

from random import random, sample

import recipe as recipe
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, CreateView, UpdateView, DetailView, ListView, FormView

from .forms import IngredientForm, CategoryForm, RecipeForm
from .models import Recipe, Ingredient, Category
from users.models import User




def show_recipes(request):
    random_recipes = None
    recipes_number = Recipe.objects.count()
    if recipes_number > 5:
        random_recipes = sample(list(Recipe.objects.all()), 5)
    else:
        random_recipes = Recipe.objects.all()
    return render(request, 'home.html', context={'recipes': random_recipes})


@login_required
def get_recipes_by_user(request):
    your_recipes = Recipe.objects.filter(author=request.user)
    data = {'recipes': your_recipes}
    return render(request, 'profile.html', context=data)


@login_required
def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            measure = form.cleaned_data['measure']
            Ingredient.objects.create(
                    name=name,
                    quantity=quantity,
                    measure=measure,
            )
    else:
        form = IngredientForm()
    context = {'title': 'Добавить ингредиент', 'form': form}
    return render(request, 'ingredient_form.html', context)


@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Category.objects.create(name=name,)
    else:
        form = CategoryForm()
    context = {'title': 'Добавить категорию', 'form': form}
    return render(request, 'category_form.html', context)


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            author = request.user
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            steps_cooking = form.cleaned_data['steps_cooking']
            time_for_cooking = form.cleaned_data['time_for_cooking']

            recipe = Recipe(
                author=author,
                title=title,
                description=description,
                steps_cooking=steps_cooking,
                time_for_cooking=time_for_cooking,
            )
            if form.cleaned_data.get('photo'):
                photo = form.cleaned_data['photo']
                fs = FileSystemStorage()
                fs.save(photo.name, photo)
                recipe.photo = photo
            recipe.save()
            ingredients_selected = form.cleaned_data['ingredients']
            print(ingredients_selected)
            for item in ingredients_selected:
                recipe.ingredients.add(item)
            if form.cleaned_data.get('categories'):
                categories_selected = list(form.cleaned_data['categories'])
                for item in categories_selected:
                    recipe.categories.add(item)
    else:
        form = RecipeForm()
    context = {'title': 'Добавить рецепт', 'form': form}
    return render(request, 'recipe_form.html', context)



class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

# class IngredientCreateView(CreateView, LoginRequiredMixin):
#     model = Ingredient
#     fields = ['name', 'quantity_kg']
#
# class CategoryCreateView(CreateView, LoginRequiredMixin):
#     model = Category
#     fields = ['name']

class RecipeDeleteView(DeleteView, LoginRequiredMixin):
    model = Recipe
    template_name = 'recipe_confirm_delete.html'
    success_url = reverse_lazy('profile')



    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author



class RecipeUpdateView(UpdateView, LoginRequiredMixin):
    model = Recipe
    template_name = 'recipe_form.html'
    fields = ['title', 'description', "steps_cooking", "time_for_cooking", "photo", "ingredients", "categories"]
    success_url = reverse_lazy('profile')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IngredientUpdateView(UpdateView
                              ,LoginRequiredMixin
                           ):

    model = Ingredient
    template_name = 'ingredient_form.html'
    fields = ['name', 'quantity', 'measure']
    success_url = reverse_lazy('profile')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def del_ingredient_from_recipe(request, id, pk):
    if request.method == 'POST':
        recipe = Recipe.objects.filter(pk=id).first()
        ingredient = Ingredient.objects.filter(pk=pk).first()
        recipe.ingredients.remove(ingredient)
        recipe.save()
    return redirect('recipe_detail', id)





    # def test_func(self):
    #     recipe = self.get_object()
    #     return self.request.user == recipe.author

