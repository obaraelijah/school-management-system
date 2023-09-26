from django.db import models
import uuid


class Course(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    course_name = models.CharField(max_length=255, unique=True)
    course_code = models.CharField(max_length=255, unique=True)
    course_description = models.TextField()
    course_credit = models.IntegerField()
    course_duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    school = models.ForeignKey("school_module.School", on_delete=models.CASCADE)
    department = models.ManyToManyField("department_module.Department", related_name="courses", null=True, blank=True)
    teacher = models.ManyToManyField("teacher_module.Teacher", related_name="courses", null=True, blank=True)
