from django.test import TestCase
from .models import Recipe
from users.models import User
from .forms import RecipeSearchForm
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


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


class RecipeSearchTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )
        self.client.login(username="testuser", password="testpass")

    # Set up non-modified objects used by all test methods
    def setUpTestData():
        Recipe.objects.create(
            name="Chocolate Cake",
            cooking_time=90,
            ingredients="flour, cocoa, eggs",
            user=User.objects.create(username="testuser", password="testpassword"),
        )
        Recipe.objects.create(
            name="Spaghetti Bolognese",
            cooking_time=30,
            ingredients="spaghetti, beef, tomatoes",
            user=User.objects.create(username="testuser", password="testpassword"),
        )
        Recipe.objects.create(
            name="Pancakes",
            cooking_time=30,
            ingredients="flour, milk, eggs",
            user=User.objects.create(username="testuser", password="testpassword"),
        )

    def test_search_term_max_length(self):
        # Create a search term that exceeds the maximum length
        long_search_term = "x" * 121  # 121 characters long, exceeding the limit

        form_data = {"search_term": long_search_term}
        form = RecipeSearchForm(data=form_data)

        # Check that the form is not valid
        self.assertFalse(form.is_valid())
        # Check that the correct error message is returned for the search_term field
        self.assertIn(
            "Ensure this value has at most 120 characters (it has 121).",
            str(form.errors["search_term"]),
        )

    def test_search_form_initialization(self):
        # Test that the search form initializes correctly
        form = RecipeSearchForm()
        self.assertTrue(form.fields["search_term"].label is None)

    def test_search_by_name(self):
        # Test searching by recipe name
        response = self.client.get(
            reverse("recipes:recipe_overview"), {"search_term": "Chocolate"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chocolate Cake")
        self.assertNotContains(response, "Spaghetti Bolognese")
        self.assertNotContains(response, "Pancakes")

    def test_search_by_ingredient(self):
        # Test searching by an ingredient
        response = self.client.get(
            reverse("recipes:recipe_overview"), {"search_term": "flour"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chocolate Cake")
        self.assertContains(response, "Pancakes")
        self.assertNotContains(response, "Spaghetti Bolognese")

    def test_show_all_recipes(self):
        # Initially, check that the number of recipes is correct
        response = self.client.get(reverse("recipes:recipe_overview"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context["object_list"]), 3
        )  # There should be 4 recipes

        # Simulate searching for a recipe
        response = self.client.get(
            reverse("recipes:recipe_overview"), {"search_term": "Pancakes"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context["object_list"]), 1
        )  # Should return 1 recipe

        # Click on the Show All button
        response = self.client.get(
            reverse("recipes:recipe_overview"), {"search_term": ""}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context["object_list"]), 3
        )  # Should return 4 recipes again


class RecipeAnalyticsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )
        self.client.login(username="testuser", password="testpass")

    # Set up non-modified objects used by all test methods
    def setUpTestData():
        Recipe.objects.create(
            name="Chocolate Cake",
            cooking_time=90,
            ingredients="flour, cocoa, eggs",
            user=User.objects.create(username="testuser", password="testpassword"),
        )
        Recipe.objects.create(
            name="Spaghetti Bolognese",
            cooking_time=30,
            ingredients="spaghetti, beef, tomatoes",
            user=User.objects.create(username="testuser", password="testpassword"),
        )
        Recipe.objects.create(
            name="Pancakes",
            cooking_time=30,
            ingredients="flour, milk, eggs",
            user=User.objects.create(username="testuser", password="testpassword"),
        )

    def test_analytics_visibility(self):
        response = self.client.get(
            reverse("recipes:recipe_overview")
        )  # Adjust the URL name if necessary
        self.assertContains(
            response, 'style="display: none;"'
        )  # Check if analytics section is initially hidden

    def test_charts_rendering(self):
        response = self.client.get(reverse("recipes:recipe_overview"))
        self.assertContains(
            response, '<img src="data:image/png;base64,'
        )  # Check if the images are present

    def test_number_of_charts(self):
        response = self.client.get(reverse("recipes:recipe_overview"))
        self.assertIsNotNone(
            response.context["bar_chart"], None
        )  # Check if bar chart data is not None
        self.assertIsNotNone(
            response.context["pie_chart"], None
        )  # Check if pie chart data is not None
        self.assertIsNotNone(
            response.context["line_chart"], None
        )  # Check if line chart data is not None

    def test_search_and_render_charts(self):
        # First, ensure there are some recipes to search
        # self.client.post(reverse('add_recipe'), data={...})  # Add test data as needed
        response = self.client.get(
            reverse("recipes:recipe_overview") + "?search_term=flour"
        )
        self.assertContains(
            response, '<img src="data:image/png;base64,'
        )  # Check if charts are still rendering

    def test_no_recipes_bar_chart(self):
        response = self.client.get(
            reverse("recipes:recipe_overview") + "?search_term=sugar"
        )
        self.assertContains(response, "No recipes available to display the bar chart.")

    def test_no_recipes_pie_chart(self):
        response = self.client.get(
            reverse("recipes:recipe_overview") + "?search_term=sugar"
        )
        self.assertContains(response, "No recipes available to display the pie chart.")

    def test_no_recipes_line_chart(self):
        response = self.client.get(
            reverse("recipes:recipe_overview") + "?search_term=sugar"
        )
        self.assertContains(response, "No recipes available to display the line chart.")

    def test_charts_visible_when_recipes_exist(self):
        response = self.client.get(reverse("recipes:recipe_overview"))
        self.assertNotContains(
            response, "No recipes available to display the bar chart."
        )
        self.assertNotContains(
            response, "No recipes available to display the pie chart."
        )
        self.assertNotContains(
            response, "No recipes available to display the line chart."
        )


class RecipeViewsProtectionsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )

        # Create a test recipe
        self.recipe = Recipe.objects.create(
            name="Test Recipe",
            cooking_time=30,
            ingredients="Ingredient 1, Ingredient 2",
            user=User.objects.create(username="testuser", password="testpassword"),
        )

    def test_recipe_list_view_login_required(self):
        # Attempt to access the recipe list view while logged out
        response = self.client.get(
            reverse("recipes:recipe_overview")
        )  # Use the appropriate URL name
        self.assertEqual(response.status_code, 302)  # Should redirect to login page

    def test_recipe_list_view_logged_in(self):
        # Log in the user
        self.client.login(username="testuser", password="testpass")

        # Access the recipe list view while logged in
        response = self.client.get(
            reverse("recipes:recipe_overview")
        )  # Use the appropriate URL name
        self.assertEqual(response.status_code, 200)  # Should return 200 OK

    def test_recipe_detail_view_login_required(self):
        # Attempt to access the recipe detail view while logged out
        response = self.client.get(
            reverse("recipes:recipe_detail", args=[self.recipe.id])
        )  # Use the appropriate URL name
        self.assertEqual(response.status_code, 302)  # Should redirect to login page

    def test_recipe_detail_view_logged_in(self):
        # Log in the user
        self.client.login(username="testuser", password="testpass")

        # Access the recipe detail view while logged in
        response = self.client.get(
            reverse("recipes:recipe_detail", args=[self.recipe.id])
        )  # Use the appropriate URL name
        self.assertEqual(response.status_code, 200)  # Should return 200 OK
