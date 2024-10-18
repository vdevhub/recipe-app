from django.test import TestCase
from .models import Recipe
from users.models import User


# Create your tests here.
class RecipeModelTest(TestCase):
    # Set up non-modified objects used by all test methods
    def setUpTestData():
        Recipe.objects.create(
            name="Tea",
            cooking_time=5,
            ingredients="tea leaves, hot water, sugar",
            user=User.objects.create(username="testuser", password="testpassword"),
        )

    def test_recipe_name(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field("name").verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, "name")
        self.assertEqual(recipe.name, "Tea")

    def test_recipe_cooking_time(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field("cooking_time").name

        # Compare the value to the expected result
        self.assertEqual(field_label, "cooking_time")
        self.assertEqual(recipe.cooking_time, 5)

    def test_recipe_ingredients(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field("ingredients").verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, "ingredients")
        self.assertEqual(recipe.ingredients, "tea leaves, hot water, sugar")

    def test_recipe_user(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field("user").verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, "user")
        self.assertEqual(recipe.user.username, "testuser")
        self.assertEqual(recipe.user.password, "testpassword")

    def test_recipe_name_max_length(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'author_name' field and use it to query its max_length
        max_length = recipe._meta.get_field("name").max_length

        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 120)

    def test_recipe_ingredients_max_length(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'author_name' field and use it to query its max_length
        max_length = recipe._meta.get_field("ingredients").max_length

        # Compare the value to the expected result i.e. 300
        self.assertEqual(max_length, 300)

    def test_recipe_difficulty_max_length(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'author_name' field and use it to query its max_length
        max_length = recipe._meta.get_field("difficulty").max_length

        # Compare the value to the expected result i.e. 12
        self.assertEqual(max_length, 12)

    def test_recipe_difficulty_value(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Compare the value to the expected result i.e. 'Easy'
        self.assertEqual(recipe.difficulty, "Easy")

    def test_recipe_str(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Compare the value to the expected result
        self.assertEqual(
            str(recipe),
            "Recipe Name: Tea\nCooking Time (Min): 5\nDifficulty: Easy\nIngredients: tea leaves, hot water, sugar",
        )

    def test_get_absolute_url(self):
        book = Recipe.objects.get(id=1)
        self.assertEqual(book.get_absolute_url(), "/recipes/overview/1")
