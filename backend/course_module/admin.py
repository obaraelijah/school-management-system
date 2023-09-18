from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name",
                    "course_code",
                    "course_description",
                    "course_credit",
                    "course_duration",
                    "school_id")


admin.site.register(Course, CourseAdmin)

# Register your models here.
