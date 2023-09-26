from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from accounts.models import Role
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CreateListDepartment(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="School Admin Can list all their departments",
        responses={
            200: "All School Departments retrieved successfully",
            403: 'User Not Authorized to perform action'},
    ) 
    def get(self, request: Request):

        user =  request.user
        role = Role.objects.filter(role_id=user.role_id).first()
        role_name = role.role_name
        if role_name != "SCHOOLADMIN" and "superuser":
            forbideen_response = {
                "status": "failed",
                "message": "user not authorized to perform this action"
            }
            return Response(forbideen_response, status=status.HTTP_403_FORBIDDEN)

        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        response = {
            "status": "success",
            "message": "All School Departments Retrieved Successfully",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="School Admin Can create a department",
        request_body=DepartmentSerializer,
        responses={
            201: "Department created successfully",
            400: 'Bad Request',
            403: 'User Not Authorized to perform action'},
    ) 
    def post(self, request: Request):

        user =  request.user
        role = Role.objects.filter(role_id=user.role_id).first()
        role_name = role.role_name
        if role_name != "SCHOOLADMIN" and "superuser":
            forbideen_response = {
                "status": "failed",
                "message": "user not authorized to perform this action"
            }
            return Response(forbideen_response, status=status.HTTP_403_FORBIDDEN)
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "Department Created Successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        bad_request_response = {
            "status": "failed",
            "message": "Department Creation Failed",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
    

class RetrieveUpdateDeleteDepartment(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="School Admin Can retrieve a specific department",
        responses={
            200: "Department  retrived successfully",
            403: 'User Not Authorized to perform action',
            404: 'Department not found'},
    ) 
    def get(self, request: Request, pk):
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
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            error_response = {
                "status": "failed",
                "message": "Department not found"
            }
            return Response(error_response, status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentSerializer(department)
        response = {
            "status": "success",
            "message": "Department Retrieved Successfully",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        operation_summary="School Admin Can update a specific department",
        request_body=DepartmentSerializer,
        responses={
            200: "Department  updated successfully",
            400: 'Bad Request',
            403: 'User Not Authorized to perform action',
            404: 'Department not found'},
    ) 
    def put(self, request: Request, pk):

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
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            error_response = {
                "status": "failed",
                "message": "Department not found"
            }
            return Response(error_response, status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentSerializer(department, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "Department Updated Successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        bad_request_response = {
            "status": "failed",
            "message": "Department Update Failed",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_summary="School Admin Can delete a specific department",
        responses={
            200: "Department  retrived successfully",
            403: 'User Not Authorized to perform action',
            404: 'Department not found'},
    ) 
    def delete(self, request: Request, pk):
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
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            error_response = {
                "status": "failed",
                "message": "Department not found"
            }
            return Response(error_response, status=status.HTTP_404_NOT_FOUND)
        department.delete()
        response = {
            "status": "success",
            "message": "Department Deleted Successfully"
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
