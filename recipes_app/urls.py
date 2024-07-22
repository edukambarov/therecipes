from django.contrib.staticfiles.urls import static
from django.urls import path, include
from .views import *
from recipes import settings

urlpatterns = [

    path('profile/', get_recipes_by_user, name='profile'),
    path('ingredient/', add_ingredient, name='add_ingredient'),
    path('category/', add_category, name='add_category'),
    path('recipe/create', add_recipe, name='add_recipe'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name="recipe_detail"),
    path('ingredient/<int:pk>/update', IngredientUpdateView.as_view(), name='ingredient_update'),
    path('ingredient/<int:id>/<int:pk>/delete', del_ingredient_from_recipe, name='ingredient_delete'),
    path('recipe/<int:pk>/update', RecipeUpdateView.as_view(), name="recipe_update"),
    path('recipe/<int:pk>/delete', RecipeDeleteView.as_view(), name="recipe_delete"),
]

