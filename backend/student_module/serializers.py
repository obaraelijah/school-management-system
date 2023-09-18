from rest_framework import serializers
from .models import Student
from department_module.models import Department
from course_module.models import Course
from school_module.models import School
from accounts.models import CustomUser
from teacher_module.models import Teacher


class StudentSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField()
    school_id = serializers.UUIDField()
    # department_id = serializers.UUIDField()
    # teacher_id = serializers.UUIDField()
    # course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)

    class Meta:
        model = Student
        fields = ["student_id",
                  "student_id_number",
                    "phone_number",
                    "date_of_birth",
                    "gender",
                    "street_address",
                    "city",
                    "state",
                    "country",
                    "school_id",
                    "user_id"
                    ]