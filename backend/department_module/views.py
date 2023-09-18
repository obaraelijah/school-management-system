from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request


class CreateListDepartment(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
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

    def get(self, request: Request, pk):
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
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def put(self, request: Request, pk):
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
    
    def delete(self, request: Request, pk):
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
