from django.urls import path
from .views import (
    home,
    about,
    RecipeListView,
    RecipeDetailView,
    recipe_add,
    recipe_add_form,
    recipe_delete,
    recipe_edit,
)

app_name = "recipes"

urlpatterns = [
    path("", home),
    path("about/", about, name="about"),
    path("recipes/overview/", RecipeListView.as_view(), name="recipe_overview"),
    path("recipes/overview/<pk>", RecipeDetailView.as_view(), name="recipe_detail"),
    path("add-form/", recipe_add_form, name="recipe_add_form"),
    path("add/", recipe_add, name="recipe_add"),
    path("delete/<int:recipe_id>/", recipe_delete, name="recipe_delete"),
    path("recipes/<int:recipe_id>/edit/", recipe_edit, name="recipe_edit"),
]
