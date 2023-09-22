from django.contrib import admin
from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_name", "school_id")


admin.site.register(Department, DepartmentAdmin)
