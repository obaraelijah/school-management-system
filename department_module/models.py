from django.db import models
import uuid
from school_module.models import School


class Department(models.Model):
    department_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    department_name = models.CharField(max_length=255, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
