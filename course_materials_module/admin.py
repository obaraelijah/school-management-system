from django.contrib import admin
from .models import CourseMaterial


class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = ("course_material_id",
                    "course_material_name",
                    "course_material_file",
                    "course",
                    "school",
                    )


admin.site.register(CourseMaterial, CourseMaterialAdmin)


