from rest_framework import serializers
from .models import NonTeachingStaff


class NonTeachingStaffSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField()
    school_id = serializers.UUIDField()

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
                    "user_id"
                    ]