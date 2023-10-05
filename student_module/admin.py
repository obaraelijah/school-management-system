from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'student_id_number', 'phone_number', 'date_of_birth', 'gender', 'school', 'user')
    

admin.site.register(Student, StudentAdmin)
