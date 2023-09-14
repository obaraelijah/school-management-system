from rest_framework import serializers
from .models import CustomUser, Role


class CustomUserSerializer(serializers.ModelSerializer):
    role_id = serializers.UUIDField()

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'last_name', 'role_id', 'is_active']
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance



class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["role_id", "role_name"]
