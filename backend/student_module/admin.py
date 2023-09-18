from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id",
                    "student_id_number",
                    "gender",
                    "school",
                    "user",
                    "department",
                    "teacher",
                    )
    

admin.site.register(Student, StudentAdmin)
