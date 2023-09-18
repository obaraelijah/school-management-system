from django.db import models
from school_module.models import School
from accounts.models import CustomUser
from department_module.models import Department
from course_module.models import Course
import uuid


class Teacher(models.Model):
    teacher_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    phone_number = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    licence_expiry_date = models.DateField()
    licence_issue_date = models.DateField()
    licence_certificate = models.ImageField(upload_to="teacher_licence_certificate")
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department = models.ManyToManyField(Department, related_name="teachers", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Assignment(models.Model):
    assignment_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    assignment_name = models.CharField(max_length=255)
    assignment_file = models.FileField(upload_to="assignments")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

