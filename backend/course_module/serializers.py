from rest_framework import serializers
from .models import Course
from department_module.models import Department  # Import the Department model
from teacher_module.models import Teacher  # Import the Teacher model

class CourseSerializer(serializers.ModelSerializer):
    school_id = serializers.UUIDField()
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), many=True)  # Handle many-to-many for department
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), many=True)  # Handle many-to-many for teacher

    class Meta:
        model = Course
        fields = [
            "course_id",
            "course_name",
            "course_code",
            "course_description",
            "course_credit",
            "course_duration",
            "school_id",
            "department",  
            "teacher"
        ]
