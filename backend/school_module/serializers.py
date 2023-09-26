from rest_framework import serializers
from .models import School
from urllib.parse import urlparse


class SchoolUpdateLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ["school_logo"]
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Remove query parameters from school_logo URL
        school_logo_url = data.get("school_logo", "")
        parsed_url = urlparse(school_logo_url)
        scheme_netloc_path = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path
        data["school_logo"] = scheme_netloc_path

        # Remove query parameters from licence_certificates URL
        # licence_certificates_url = data.get("school_licence_certificate", "")
        # parsed_url = urlparse(licence_certificates_url)
        # scheme_netloc_path = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path
        # data["school_licence_certificate"] = scheme_netloc_path

        return data


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            "school_id",
            "school_name",
            "school_email",
            "school_logo",
            "school_phone_number",
            "school_address",
            "school_city",
            "school_state",
            "school_postal_code",
            "school_country"
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Remove query parameters from school_logo URL
        school_logo_url = data.get("school_logo", "")
        parsed_url = urlparse(school_logo_url)
        scheme_netloc_path = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path
        data["school_logo"] = scheme_netloc_path

        # Remove query parameters from licence_certificates URL
        # licence_certificates_url = data.get("school_licence_certificate", "")
        # parsed_url = urlparse(licence_certificates_url)
        # scheme_netloc_path = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path
        # data["school_licence_certificate"] = scheme_netloc_path

        return data




