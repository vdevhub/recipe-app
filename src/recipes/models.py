from django.db import models
from users.models import User


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.PositiveBigIntegerField()
    ingredients = models.CharField(
        max_length=300, help_text="Enter the ingredients as comma-separated list"
    )
    difficulty = models.CharField(max_length=12, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Calculate the difficulty before saving
        ingredients_count = len(self.ingredients.split(", "))
        if self.cooking_time < 10:
            if ingredients_count < 4:
                self.difficulty = "Easy"
            else:
                self.difficulty = "Medium"
        elif self.cooking_time >= 10:
            if ingredients_count < 4:
                self.difficulty = "Intermediate"
            else:
                self.difficulty = "Hard"

        # Call the real save() method
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return (
            "Recipe Name: "
            + self.name
            + "\nCooking Time (Min): "
            + str(self.cooking_time)
            + "\nDifficulty: "
            + self.difficulty
            + "\nIngredients: "
            + self.ingredients
        )
