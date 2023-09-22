from rest_framework import serializers
from .models import Teacher, Assignment
from department_module.models import Department


class TeacherSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), many=True)

    class Meta:
        model = Teacher
        fields = ["teacher_id",
                  "phone_number",
                  "date_of_birth",
                  "gender",
                  "license_number",
                  "licence_expiry_date",
                  "licence_issue_date",
                  "street_address",
                  "city",
                  "state",
                  "country",
                  "school_id",
                  "user_id",
                  "department"
                ]


class AssignmentSerializer(serializers.ModelSerializer):
    school_id = serializers.UUIDField()
    course_id = serializers.UUIDField()
    teacher_id = serializers.UUIDField()
    department = serializers.UUIDField()

    class Meta:
        model = Assignment
        fields = [
            "assignment_id",
            "assignment_name",
            "assignment_file",
            "school_id",
            "teacher",
            "course",
            "department"
        ]

    
        