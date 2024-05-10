from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from base.admin import BaseAdmin
from . import models


@admin.register(models.User)
class UserAdmin(DefaultUserAdmin, BaseAdmin):
    list_display = ["id", "email", "name", "mobile_number"]
    list_filter = ["date_joined"]
    search_fields = ["email"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {"fields": ("name", "mobile_number")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_superuser",
                    "is_staff",
                    "user_permissions",
                )
            },
        ),
    )

    ordering = ("id",)
