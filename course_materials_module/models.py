from django.db import models
from school_module.models import School
from course_module.models import Course
import uuid


class CourseMaterial(models.Model):
    course_material_id = models.UUIDField(primary_key=True,
                                          editable=False,
                                          default=uuid.uuid4,
                                          unique=True)
    course_material_name = models.CharField(max_length=255)
    course_material_file = models.FileField(upload_to="course_materials")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
