from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, recipe_add, recipe_add_form

app_name = "recipes"

urlpatterns = [
    path("", home),
    path("recipes/overview/", RecipeListView.as_view(), name="recipe_overview"),
    path("recipes/overview/<pk>", RecipeDetailView.as_view(), name="recipe_detail"),
    path("add-form/", recipe_add_form, name="recipe_add_form"),
    path("add/", recipe_add, name="recipe_add"),
]
