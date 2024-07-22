from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Recipe, Ingredient, Category


class IngredientForm(forms.Form):
    name = forms.CharField(max_length=50)
    quantity = forms.IntegerField()
    measure = forms.ChoiceField(choices=Ingredient.MEASURES)

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
    name = forms.CharField(max_length=50)


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    steps_cooking = forms.CharField(widget=forms.Textarea)
    ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all(),
                                                 widget=forms.CheckboxSelectMultiple
                                                 (attrs={'class': 'form-check_input'}))
    categories = forms.ModelMultipleChoiceField(required=False,
                                                queryset=Category.objects.all(),
                                                widget=forms.CheckboxSelectMultiple
                                                (attrs={'class': 'form-check_input'}))
    time_for_cooking = forms.IntegerField(min_value=0)
    photo = forms.ImageField(required=False)


