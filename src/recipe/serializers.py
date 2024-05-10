from rest_framework import serializers
from . import models


class RecipeSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="owner.name", read_only=True)

    class Meta:
        model = models.Recipe
        fields = [
            "title",
            "description",
            "ingredients",
            "preparation_steps",
            "cooking_time",
            "serving_size",
            "categories",
            "slug",
            "author_name",
            "id",
        ]
        extra_kwargs = {'slug': {'read_only': True}}

    def create(self, validated_data):
        validated_data["owner"] = self.context["user"]
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.owner = self.context["user"]
        return super().update(instance, validated_data)


class RatingSerializer(serializers.ModelSerializer):
    recipe_details = serializers.SerializerMethodField(read_only=True)
    user_name = serializers.CharField(source="user.name", read_only=True)
    user_email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = models.Rating
        fields = [
            "recipe_details",
            "recipe",
            "user",
            "rating",
            "user_email",
            "user_name",
            "id"
        ]

    def get_recipe_details(self, obj):
        return RecipeSerializer(instance=obj).data


class ReviewSerializer(serializers.ModelSerializer):
    recipe_details = serializers.SerializerMethodField(read_only=True)
    user_name = serializers.CharField(source="user.name", read_only=True)
    user_email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = models.Review
        fields = [
            "text",
            "user_email",
            "user_name",
            "recipe_details",
            "id"
        ]


class RecipeCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RecipeCategory
        fields = ["name", "id"]
