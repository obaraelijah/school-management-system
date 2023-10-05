from django.contrib import admin
from .models import Teacher, Assignment


# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ("teacher_id", "school_id", "user_id")


admin.site.register(Teacher)
admin.site.register(Assignment)



class AssignmentAdmin(admin.ModelAdmin):
    ...

