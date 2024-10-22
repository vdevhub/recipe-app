from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin

# to protect function-based views
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "recipes/recipes_home.html")


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipes_overview.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = context["recipe"]

        # Split ingredients by commas
        context["ingredients_list"] = [
            ingredient.strip() for ingredient in recipe.ingredients.split(",")
        ]

        return context
