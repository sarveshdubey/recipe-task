import django_filters

from base import filters
from . import models


class RecipeFilter(filters.BaseFilter):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")
    category = django_filters.CharFilter(field_name="category__name", lookup_expr="icontains")
    user_username = django_filters.CharFilter(field_name="user__username", lookup_expr="icontains")
    recipe_id = django_filters.CharFilter(field_name="id")
    user_email = django_filters.CharFilter(field_name="user__email")

    class Meta:
        model = models.Recipe
        fields = ["title", "description", "category", "user_username", "recipe_id", "user_email"]


class RatingFilter(filters.BaseFilter):
    recipe = django_filters.CharFilter(field_name="recipe__title", lookup_expr="icontains")
    user = django_filters.CharFilter(field_name="user__username", lookup_expr="icontains")
    min_rating = django_filters.NumberFilter(field_name="rating", lookup_expr="gte")
    max_rating = django_filters.NumberFilter(field_name="rating", lookup_expr="lte")

    class Meta:
        model = models.Rating
        fields = ["recipe", "user", "min_rating", "max_rating"]


class ReviewFilter(filters.BaseFilter):
    recipe_title = django_filters.CharFilter(field_name="recipe__title", lookup_expr="icontains")
    user_username = django_filters.CharFilter(field_name="user__username", lookup_expr="icontains")
    recipe_id = django_filters.CharFilter(field_name="recipe__id")
    user_email = django_filters.CharFilter(field_name="user__email")

    class Meta:
        model = models.Review
        fields = ["recipe_title", "user_username", "recipe_id", "user_email"]


class RecipeCategoryFilter(filters.BaseFilter):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = models.RecipeCategory
        fields = ["name"]
