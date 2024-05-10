from django.urls import include, path
from rest_framework import routers

from src.recipe import views

router = routers.DefaultRouter(trailing_slash=False)
router.register("recipe", views.RecipeViewSet, basename="recipe")
router.register("category", views.RecipeCategoryViewSet, basename="category")
router.register("rating", views.RatingViewSet, basename="rating")
router.register("review", views.ReviewViewSet, basename="review")


urlpatterns = [
    path("", include(router.urls)),
]
