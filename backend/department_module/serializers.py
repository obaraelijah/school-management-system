from rest_framework import serializers
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    school_id = serializers.UUIDField()
    
    class Meta:
        model = Department
        fields = ["department_id", "department_name", "school_id"]