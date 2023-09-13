from django.contrib import admin
from .models import School


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'school_email', 'school_logo', 'school_phone_number', 'school_address')


admin.site.register(School, SchoolAdmin)
