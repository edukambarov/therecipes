from django.urls import path, include

from .views import Register
    # Home
from recipes_app.views import show_recipes

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', show_recipes, name='home'),
    # path('', Home.as_view(), name='home'),
    path('register/', Register.as_view(), name='register'),
]