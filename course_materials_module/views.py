from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import CourseMaterial
from .serializers import CourseMaterialSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from accounts.models import Role


class CreateListCourseMaterialView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_summary="School Admin can retrieve all course materials",
        responses={
            200: "All Course materials retrived successfully",
            403: 'User Not Authorized to perform action'},
    )
    def get(self, request: Request):
        user = request.user
        role = Role.objects.filter(role_id=user.role_id).first()
        role_name = role.role_name
        if role_name != "SCHOOLADMIN" and "superuser":
            forbideen_response = {
                "status": "failed",
                "message": "user not authorized to perform this action"
            }
            return Response(forbideen_response, status=status.HTTP_403_FORBIDDEN)
        course_materials = CourseMaterial.objects.all()
        serializer = CourseMaterialSerializer(course_materials, many=True)
        response = {
            "status": "success",
            "message": "All course materials retrieved successfully",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="School Admin Can create a course material",
        request_body=CourseMaterialSerializer,
        responses={
            201: "Course material created successfully",
            400: 'Bad Request',
            403: 'User Not Authorized to perform action'},
    )
    def post(self, request):
        user = request.user
        role = Role.objects.filter(role_id=user.role_id).first()
        role_name = role.role_name
        if role_name != "SCHOOLADMIN" and "superuser":
            forbideen_response = {
                "status": "failed",
                "message": "user not authorized to perform this action"
            }
            return Response(forbideen_response, status=status.HTTP_403_FORBIDDEN)
        serializer = CourseMaterialSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                "status": "success",
                "message": "Course material created successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        bad_request_response = {
            "status": "error",
            "message": "Bad request",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
    

class RetrieveUpdateDestroyCourseMaterialView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_summary="School Admin Can retrieve a specific course material",
        responses={
            200: "Course material retrieved successfully",
            403: 'User Not Authorized to perform action',
            404: 'Course material does not exist'},
    )
    def get(self, request: Request, pk):
        user = request.user
        role = Role.objects.filter(role_id=user.role_id).first()
        role_name = role.role_name
        if role_name != "SCHOOLADMIN" and "superuser":
            forbideen_response = {
                "status": "failed",
                "message": "user not authorized to perform this action"
            }
            return Response(forbideen_response, status=status.HTTP_403_FORBIDDEN)
        try:
            course_material = CourseMaterial.objects.get(pk=pk)
            serializer = CourseMaterialSerializer(course_material)
            response = {
                "status": "success",
                "message": "Course material retrieved successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        except CourseMaterial.DoesNotExist:
            response = {
                "status": "error",
                "message": "Course material does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="School Admin Can update a specific course material",
        request_body=CourseMaterialSerializer,
        responses={
            200: "Course material updated successfully",
            400: 'Bad Request',
            403: 'User Not Authorized to perform action',
            404: 'Course material does not exist'},
    )    
    def put(self, request: Request, pk):
        user = request.user
        role = Role.objects.filter(role_id=user.role_id).first()
        role_name = role.role_name
        if role_name != "SCHOOLADMIN" and "superuser":
            forbideen_response = {
                "status": "failed",
                "message": "user not authorized to perform this action"
            }
            return Response(forbideen_response, status=status.HTTP_403_FORBIDDEN)
        try:
            course_material = CourseMaterial.objects.get(pk=pk)
            serializer = CourseMaterialSerializer(course_material, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                response = {
                    "status": "success",
                    "message": "Course material updated successfully",
                    "data": serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
        except CourseMaterial.DoesNotExist:
            response = {
                "status": "error",
                "message": "Course material does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="School Admin Can delete a specific course material",
        responses={
            204: "Course material deleted successfully",
            403: 'User Not Authorized to perform action',
            404: 'Course material does not exist'},
    ) 
    def delete(self, request: Request, pk):
        user = request.user
        role = Role.objects.filter(role_id=user.role_id).first()
        role_name = role.role_name
        if role_name != "SCHOOLADMIN" and "superuser":
            forbideen_response = {
                "status": "failed",
                "message": "user not authorized to perform this action"
            }
            return Response(forbideen_response, status=status.HTTP_403_FORBIDDEN)
        try:
            course_material = CourseMaterial.objects.get(pk=pk)
            course_material.delete()
            response = {
                "status": "success",
                "message": "Course material deleted successfully"
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        except CourseMaterial.DoesNotExist:
            response = {
                "status": "error",
                "message": "Course material does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
