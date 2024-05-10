from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from src.user import models


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = models.User
        fields = [
            "id",
            "name",
            "email",
            "mobile_number",
            "password",
            "confirm_password",
            "response_message",
        ]

    def validate(self, data):
        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def validate_mobile_number(self, value):
        if models.User.objects.filter(mobile_number=value).exists():
            raise serializers.ValidationError(
                {"password": "User with this mobile number already exists."}
            )

        return value

    def validate_email(self, value):
        if models.User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                {"email": "User with this email already exists."}
            )
        return value

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        confirm_password = validated_data.pop("confirm_password", None)

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        user = models.User.objects.create_user(password=password, **validated_data)

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        if password:
            instance.set_password(password)

        super().update(instance, validated_data)

        return instance
