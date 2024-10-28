from django import forms
from .models import Recipe


class RecipeSearchForm(forms.Form):
    search_term = forms.CharField(
        max_length=120,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name or ingredient..."}
        ),
    )


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "cooking_time", "ingredients", "directions", "pic"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Recipe Name"}),
            "cooking_time": forms.NumberInput(
                attrs={"placeholder": "Cooking Time (in minutes)"}
            ),
            "ingredients": forms.Textarea(
                attrs={"placeholder": "Enter ingredients separated by commas"}
            ),
            "directions": forms.Textarea(
                attrs={"placeholder": "Enter recipe directions"}
            ),
        }
        # Set help_text to empty for all fields to prevent display
        help_texts = {
            "name": "",
            "cooking_time": "",
            "ingredients": "",
            "directions": "",
            "pic": "",
        }
