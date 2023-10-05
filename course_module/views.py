from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from accounts.models import Role
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CreateListCourse(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="School Admin can retrieve all courses",
        responses={
            200: "All Courses retrived successfully",
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
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        response = {
            "status": "success",
            "message": "All Courses Retrieved Successfully",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="School Admin Can create a course",
        request_body=CourseSerializer,
        responses={
            201: "Course created successfully",
            400: 'Bad Request',
            403: 'User Not Authorized to perform action'},
    )
    def post(self, request: Request):
        user = request.user
        role = Role.objects.filter(role_id=user.role_id).first()
        role_name = role.role_name
        if role_name != "SCHOOLADMIN" and "superuser":
            forbideen_response = {
                "status": "failed",
                "message": "user not authorized to perform this action"
            }
            return Response(forbideen_response, status=status.HTTP_403_FORBIDDEN)
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "Course Created Successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        bad_request_response = {
            "status": "failed",
            "message": "Course Creation Failed",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDeleteCourse(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="School Admin can retrieve a specific course",
        responses={
            200: "Course retrieved successfully",
            403: 'User Not Authorized to perform action',
            404: 'Course does not exist'},
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
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            error_response = {
                "status": "failed",
                "message": "Course not found"
            }
            return Response(error_response, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course)
        response = {
            "status": "success",
            "message": "Course Retrieved Successfully",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        operation_summary="School Admin Can update a specific course",
        request_body=CourseSerializer,
        responses={
            200: "Course updated successfully",
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
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            error_response = {
                "status": "failed",
                "message": "Course not found"
            }
            return Response(error_response, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "Course Updated Successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        bad_request_response = {
            "status": "failed",
            "message": "Course Update Failed",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_summary="School Admin Can delete a specific course",
        responses={
            204: "Course deleted successfully",
            403: 'User Not Authorized to perform action',
            404: 'Course does not exist'},
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
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            error_response = {
                "status": "failed",
                "message": "Course not found"
            }
            return Response(error_response, status=status.HTTP_404_NOT_FOUND)
        course.delete()
        response = {
            "status": "success",
            "message": "Course Deleted Successfully"
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
