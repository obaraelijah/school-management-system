from rest_framework import serializers
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    school_id = serializers.UUIDField()
    school_name = serializers.CharField(source='school.school_name', read_only=True)
    
    class Meta:
        model = Department
        fields = ["department_id",
                  "department_name",
                  "school_id",
                  "school_name"]