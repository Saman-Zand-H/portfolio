from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.decorators import register

from .models import UserModel


@register(UserModel)
class UserAdmin(UserAdmin):
    readonly_fields = ["date_joined"]
    sortable_by = ["username", "date_joined", "last_login"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "picture"
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = ((
        None,
        {
            "fields": (
                "username",
                "email",
                "first_name",
                "last_name",
                "picture",
                "password1",
                "password2",
            ),
            "classes": "wide",
        },
    ), )
    list_display = ["name", "username"]
    search_fields = ["name", "username"]
    filter_horizontal = ["groups", "user_permissions"]
    
