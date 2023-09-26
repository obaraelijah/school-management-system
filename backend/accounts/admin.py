from django.contrib import admin
from .models import CustomUser, Role


class AccountsAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "is_active"
    )


class RoleAdmin(admin.ModelAdmin):
    list_display = ("role_name",)


admin.site.register(CustomUser, AccountsAdmin)

admin.site.register(Role, RoleAdmin)
