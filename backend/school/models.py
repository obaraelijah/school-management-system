from django.db import models
import uuid


class School(models.Model):
    school_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school_name = models.CharField(max_length=255, unique=True)
    school_email = models.EmailField(unique=True)
    school_phone_number = models.CharField(max_length=255)
    school_licence_number = models.CharField(max_length=255, unique=True)
    school_licence_certificate = models.FileField(upload_to='licence_certificates/')
    school_logo = models.ImageField(upload_to='school_logos/')
    school_address = models.CharField(max_length=255)
    school_city = models.CharField(max_length=255)
    school_state = models.CharField(max_length=255)
    school_postal_code = models.CharField(max_length=255)
    school_country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.school_name
  
    class Meta:
        ordering = ['school_name']

