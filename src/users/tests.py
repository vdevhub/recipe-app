from django.test import TestCase
from .models import User


# Create your tests here.
class UserModelTest(TestCase):
    # Set up non-modified objects used by all test methods
    def setUpTestData():
        User.objects.create(username="testuser", password="testpassword")

    def test_user_name(self):
        # Get a user object to test
        user = User.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = user._meta.get_field("username").verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, "username")
        self.assertEqual(user.username, "testuser")

    def test_user_password(self):
        # Get a user object to test
        user = User.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = user._meta.get_field("password").verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, "password")
        self.assertEqual(user.password, "testpassword")

    def test_user_str(self):
        # Get a user object to test
        user = User.objects.get(id=1)

        # Compare the value to the expected result
        self.assertEqual(str(user), "testuser")
        self.assertEqual(str(user), user.username)
