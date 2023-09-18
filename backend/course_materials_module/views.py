from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import CourseMaterial
from .serializers import CourseMaterialSerializer
from rest_framework.permissions import IsAuthenticated


class CreateListCourseMaterialView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request):
        course_materials = CourseMaterial.objects.all()
        serializer = CourseMaterialSerializer(course_materials, many=True)
        response = {
            "status": "success",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
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

    def get(self, request: Request, pk):
        try:
            course_material = CourseMaterial.objects.get(pk=pk)
            serializer = CourseMaterialSerializer(course_material)
            response = {
                "status": "success",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        except CourseMaterial.DoesNotExist:
            response = {
                "status": "error",
                "message": "Course material does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request: Request, pk):
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
     
    def delete(self, request: Request, pk):
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
