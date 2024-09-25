from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Recipe, Ingredient, Category


class IngredientForm(forms.Form):
    name = forms.CharField(label='Название ингредиента', max_length=50)
    quantity = forms.IntegerField(label='Количество')
    measure = forms.ChoiceField(label='Единица измерения', choices=Ingredient.MEASURES)

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is None:
            return self.fields['quantity'].initial
        else:
            return quantity

    def clean_measure(self):
        measure = self.cleaned_data.get('measure')
        if measure is None:
            return self.fields['measure'].initial
        else:
            return measure


class CategoryForm(forms.Form):
    name = forms.CharField(label='Название категории',max_length=50)


class RecipeForm(forms.Form):
    title = forms.CharField(label='Название блюда',
                                                max_length=100)
    description = forms.CharField(label='Описание',
                                                widget=forms.Textarea)
    steps_cooking = forms.CharField(label='Шаги приготовления',
                                                widget=forms.Textarea)
    ingredients = forms.ModelMultipleChoiceField(label='Ингредиенты',
                                                queryset=Ingredient.objects.all(),
                                                 widget=forms.CheckboxSelectMultiple
                                                 (attrs={'class': 'form-check_input'}))
    categories = forms.ModelMultipleChoiceField(label='Категории',
                                                required=False,
                                                queryset=Category.objects.all(),
                                                widget=forms.CheckboxSelectMultiple
                                                (attrs={'class': 'form-check_input'}))
    time_for_cooking = forms.IntegerField(label='Время приготовления',
                                                 min_value=0)
    photo = forms.ImageField(label='Изображение',required=False)


