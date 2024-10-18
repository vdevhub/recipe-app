from django.urls import path
from .views import home, RecipeListView, RecipeDetailView

app_name = "recipes"

urlpatterns = [
    path("", home),
    path("recipes/overview/", RecipeListView.as_view(), name="recipe_overview"),
    path("recipes/overview/<pk>", RecipeDetailView.as_view(), name="recipe_detail"),
]
