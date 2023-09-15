from .base import *
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = True

SECRET_KEY = ""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

AWS_ACCESS_KEY_ID= ""
AWS_SECRET_ACCESS_KEY= ""
AWS_STORAGE_BUCKET_NAME=""
AWS_S3_REGION_NAME= ""
AWS_S3_FILE_OVERWRITE= False
AWS_DEFAULT_ACL = None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
