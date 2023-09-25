from rest_framework import serializers
from .models import NonTeachingStaff


class NonTeachingStaffSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField()
    user_first_name = serializers.CharField(source="user.first_name", read_only=True)
    user_last_name = serializers.CharField(source="user.last_name", read_only=True)
    school_id = serializers.UUIDField()
    school_name = serializers.CharField(source="school.school_name", read_only=True)

    class Meta:
        model = NonTeachingStaff
        fields = ["non_teaching_staff_id",
                  "phone_number",
                  "gender",
                    "date_of_birth",
                    "street_address",
                    "city",
                    "state",
                    "country",
                    "school_id",
                    "school_name",
                    "user_id",
                    "user_first_name",
                    "user_last_name"
                    ]