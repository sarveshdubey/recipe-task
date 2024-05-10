from django.db import models
from django.utils.text import slugify

from base.models import BaseModel
from src.user.models import User


class RecipeCategory(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    preparation_steps = models.TextField()
    cooking_time = models.PositiveIntegerField()  # in minutes
    serving_size = models.PositiveIntegerField()
    categories = models.ManyToManyField(RecipeCategory, related_name='recipes')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    slug = models.SlugField(unique=True)  # Unique slug for public sharing

    @property
    def response_message(self) -> str:
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    # created_at field removed as it's in BaseModel

    @property
    def response_message(self) -> str:
        return f"{self.rating} by {self.user.username}"


class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()

    @property
    def response_message(self) -> str:
        return f"Review for {self.recipe.title} by {self.user.username}"
