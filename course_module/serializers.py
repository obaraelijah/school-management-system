from rest_framework import serializers
from .models import Course
from department_module.models import Department  # Import the Department model
from teacher_module.models import Teacher  # Import the Teacher model

class CourseSerializer(serializers.ModelSerializer):
    school_id = serializers.UUIDField()
    school_name = serializers.CharField(source='school.school_name', read_only=True)
    departments = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), many=True)  # Handle many-to-many for department
    #teachers = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), many=True)  # Handle many-to-many for teacher
    
    departments_name = serializers.SerializerMethodField()  # Handle many-to-many for department
    #teachers_name = serializers.SerializerMethodField()  # Handle many-to-many for teacher
    
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
            "school_name",
            "departments", 
            "departments_name", 
            #"teachers",
            # "teachers_name"
        ]

    def get_departments_name(self, obj):  # Handle many-to-many for department
        return [department.department_name for department in obj.departments.all()]
    
    # def get_teachers_name(self, obj):  # Handle many-to-many for teacher
    #     return [teacher.teacher_name for teacher in obj.teachers.all()]
