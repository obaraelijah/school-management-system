from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from .models import School
from accounts.models import Role, CustomUser
from .serializers import SchoolSerializer, SchoolUpdateLogoSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CreateAndListSchool(APIView):
    """
    CreateAndListSchool class handles the creation and listing of schools.

    POST: Create a new school.
    GET: Retrieve a list of all schools.
    """
    permission_classes = [IsAdminUser]

    def post(self, request: Request):
        """
        POST method to create a new school.
        """
        data = request.data
        serializer = SchoolSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
    def get(self, request: Request):
        """
        GET method to retrieve a list of all schools.
        """
        queryset = School.objects.all()
        serializer = SchoolSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveUpdateDeleteSchool(APIView):
    """
    RetrieveUpdateDeleteSchool class handles the retrieval, updating, and deletion of schools.

    GET: Retrieve detailed information about a specific school.
    PUT: Update school information (allows partial updates).
    DELETE: Delete a specific school.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk):
        """
        GET method to retrieve detailed information about a specific school by using it's id.
        """
        try:
            queryset = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return Response({"error": "School not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SchoolSerializer(instance=queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request: Request, pk):
        """
        PUT method to update school information (allows partial updates) by using it's id.
        """
        try:
            queryset = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return Response({"error": "School not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializer = SchoolSerializer(instance=queryset, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk):
        """
        DELETE method to delete a specific school using it's id.
        """
        try:
            queryset = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return Response({"error": "School not found"}, status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UpdateSchoolLogo(APIView):
    """
    UpdateSchoolLogo class handles the updating of the school's logo.

    PUT: Update the school's logo.
    """
    permission_classes = [IsAuthenticated]

    def put(self, request: Request, pk):
        """
        PUT method to update the school's logo.
        """
        try:
            queryset = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return Response({"error": "School not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializer = SchoolUpdateLogoSerializer(instance=queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




