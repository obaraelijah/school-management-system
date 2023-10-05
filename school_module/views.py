from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from .models import School
from accounts.models import Role, CustomUser
from .serializers import SchoolSerializer, SchoolUpdateLogoSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CreateAndListSchool(APIView):
    """
    CreateAndListSchool class handles the creation and listing of schools.

    POST: Create a new school.
    GET: Retrieve a list of all schools.
    """
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary=" Admin Create a new school",
        request_body=SchoolSerializer,
        responses={
            201: "School created successfully",
            400: 'Bad Request',
            403: 'User Not Authorized to perform action'},
    ) 
    def post(self, request: Request):
        """
        POST method to create a new school.
        """
        data = request.data
        serializer = SchoolSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "School Created Successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        bad_request_response = {
            "status": "failed",
            "message": "School Creation Failed",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Admin retrieve all schools",
        responses={
            200: "All Schools  retrived successfully",
            400: 'Bad Request',
            403: 'User Not Authorized to perform action'},
    )  
    def get(self, request: Request):
        """
        GET method to retrieve a list of all schools.
        """
        queryset = School.objects.all()
        serializer = SchoolSerializer(instance=queryset, many=True)
        response = {
            "status": "success",
            "message": "All Schools Retrieved Successfully",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)


class RetrieveUpdateDeleteSchool(APIView):
    """
    RetrieveUpdateDeleteSchool class handles the retrieval, updating, and deletion of schools.

    GET: Retrieve detailed information about a specific school.
    PUT: Update school information (allows partial updates).
    DELETE: Delete a specific school.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="School Admin Can retrieve their specific school",
        responses={
            200: "School Retrieved successfully",
            404: 'School not found',
            403: 'User Not Authorized to perform action'},
    ) 
    def get(self, request: Request, pk):
        """
        GET method to retrieve detailed information about a specific school by using it's id.
        """
        user =  request.user
        role = Role.objects.filter(role_id=user.role_id).first()
        role_name = role.role_name
        if role_name != "SCHOOLADMIN" and "superuser":
            forbideen_response = {
                "status": "failed",
                "message": "user not authorized to perform this action"
            }
            return Response(forbideen_response, status=status.HTTP_403_FORBIDDEN)

        try:
            queryset = School.objects.get(pk=pk)
        except School.DoesNotExist:
            not_found_response = {
                "status": "failed",
                "message": "School not found"
            }
            return Response(not_found_response, status=status.HTTP_404_NOT_FOUND)
        serializer = SchoolSerializer(instance=queryset)
        response = {
            "status": "success",
            "message": "School Retrieved Successfully",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        operation_summary="School Admin Can update their specific school",
        request_body=SchoolSerializer,
        responses={
            200: "School updated successfully",
            400: 'Bad Request',
            403: 'User Not Authorized to perform action',
            404: 'School not found'},
    ) 
    def put(self, request: Request, pk):
        """
        PUT method to update school information (allows partial updates) by using it's id.
        """
        user =  request.user
        role = Role.objects.filter(role_id=user.role_id).first()
        role_name = role.role_name
        if role_name != "SCHOOLADMIN" and "superuser":
            forbideen_response = {
                "status": "failed",
                "message": "user not authorized to perform this action"
            }
            return Response(forbideen_response, status=status.HTTP_403_FORBIDDEN)

        try:
            queryset = School.objects.get(pk=pk)
        except School.DoesNotExist:
            not_found_response = {
                "status": "failed",
                "message": "School not found"
            }
            return Response(not_found_response, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializer = SchoolSerializer(instance=queryset, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "School Updated Successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        bad_request_response = {
            "status": "failed",
            "message": "School Update Failed",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_summary="School Admin Can delete their specific school",
        responses={
            204: "School deleted successfully",
            403: 'User Not Authorized to perform action',
            404: 'School not found'},
    )
    def delete(self, request: Request, pk):
        """
        DELETE method to delete a specific school using it's id.
        """
        user =  request.user
        role = Role.objects.filter(role_id=user.role_id).first()
        role_name = role.role_name
        if role_name != "SCHOOLADMIN" and "superuser":
            forbideen_response = {
                "status": "failed",
                "message": "user not authorized to perform this action"
            }
            return Response(forbideen_response, status=status.HTTP_403_FORBIDDEN)

        try:
            queryset = School.objects.get(pk=pk)
        except School.DoesNotExist:
            not_found_response = {
                "status": "failed",
                "message": "School not found"
            }
            return Response(not_found_response, status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        response = {
            "status": "success",
            "message": "School Deleted Successfully"
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
    

class UpdateSchoolLogo(APIView):
    """
    UpdateSchoolLogo class handles the updating of the school's logo.

    PUT: Update the school's logo.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="School Admin Can update their specific school logo",
        request_body=SchoolUpdateLogoSerializer,
        responses={
            200: "school logo updated successfully",
            400: 'Bad Request',
            403: 'User Not Authorized to perform action',
            404: 'School not found'},
    )
    def put(self, request: Request, pk):
        """
        PUT method to update the school's logo.
        """
        user =  request.user
        role = Role.objects.filter(role_id=user.role_id).first()
        role_name = role.role_name
        if role_name != "SCHOOLADMIN" and "superuser":
            forbideen_response = {
                "status": "failed",
                "message": "user not authorized to perform this action"
            }
            return Response(forbideen_response, status=status.HTTP_403_FORBIDDEN)

        try:
            queryset = School.objects.get(pk=pk)
        except School.DoesNotExist:
            not_found_response = {
                "status": "failed",
                "message": "School not found"
            }
            return Response(not_found_response, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializer = SchoolUpdateLogoSerializer(instance=queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "School Logo Updated Successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        bad_request_response = {
            "status": "failed",
            "message": "School Logo Update Failed",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
    




