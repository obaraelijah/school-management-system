from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from .models import CustomUser, Role
from .serializers import CustomUserSerializer, RoleSerializer


class CreateListRoles(APIView):
    
    def post(self, request: Request):
        data = request.data
        serializer = RoleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request: Request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveUpdateRole(APIView):
    
    def get(self, request: Request, pk):
        try:
            queryset = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            return Response({"error": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RoleSerializer(instance=queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request: Request, pk):
        try:
            queryset = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            return Response({"error": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializer = RoleSerializer(queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CreateRetrieveUsers(APIView):

    def post(self, request: Request):
        data = request.data
        serializer = CustomUserSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request: Request):
        queryset = CustomUser.objects.all()
        serializer = CustomUserSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveUpdateDeleteUser(APIView):
    
    def get(self, request: Request, pk):
        try:
            queryset = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CustomUserSerializer(instance=queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request: Request, pk):
        try:
            queryset = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializer = CustomUserSerializer(queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk):
        try:
            queryset = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

