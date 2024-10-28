from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Recipe

# to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin

# to protect function-based views
from django.contrib.auth.decorators import login_required

# to search and query results
from .forms import RecipeSearchForm, RecipeForm
from django.db.models import Q
import pandas as pd

from .utils import plot_bar_chart, plot_pie_chart, plot_line_chart
from django.http import JsonResponse
from django.contrib.auth import get_user


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
        # Get the current recipes displayed
        current_recipes = self.get_queryset()

        # Generate charts based on the current recipes
        context["bar_chart"] = plot_bar_chart(current_recipes)
        context["pie_chart"] = plot_pie_chart(current_recipes)
        context["line_chart"] = plot_line_chart(current_recipes)
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


@login_required
def recipe_add_form(request):
    form = RecipeForm()
    return render(request, "recipes/partials/recipe_form.html", {"form": form})


@login_required
def recipe_add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return JsonResponse({"status": "success"}, status=200)
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
