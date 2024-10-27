from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin

# to protect function-based views
from django.contrib.auth.decorators import login_required

# to search and query results
from .forms import RecipeSearchForm
from django.db.models import Q
import pandas as pd


# Create your views here.
def home(request):
    return render(request, "recipes/recipes_home.html")


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipes_overview.html"
    context_object_name = "recipes"

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get the search term from the GET request
        search_term = self.request.GET.get("search_term", "").strip()

        if search_term:
            # Filter recipes by name or ingredients if a search term is provided
            queryset = queryset.filter(
                Q(name__icontains=search_term) | Q(ingredients__icontains=search_term)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the search form with the current search term (if any)
        context["form"] = RecipeSearchForm(
            initial={"search_term": self.request.GET.get("search_term", "")}
        )
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add search form to context
        context["form"] = RecipeSearchForm(
            self.request.GET or None
        )  # Prefill with search term if available
        return context


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
