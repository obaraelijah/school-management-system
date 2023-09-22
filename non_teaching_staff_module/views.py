from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import NonTeachingStaff
from .serializers import NonTeachingStaffSerializer
from rest_framework.permissions import IsAuthenticated


class CreateListNonTeachingStaffView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request):
        non_teaching_staff = NonTeachingStaff.objects.all()
        serializer = NonTeachingStaffSerializer(non_teaching_staff, many=True)
        response = {
            "status": "success",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NonTeachingStaffSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                "status": "success",
                "message": "Non teaching staff created successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        bad_request_response = {
            "status": "error",
            "message": "Bad request",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
    

class RetrieveUpdateDestroyNonTeachingStaffView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request, pk):
        try:
            non_teaching_staff = NonTeachingStaff.objects.get(pk=pk)
            serializer = NonTeachingStaffSerializer(non_teaching_staff)
            response = {
                "status": "success",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        except NonTeachingStaff.DoesNotExist:
            response = {
                "status": "error",
                "message": "Non teaching staff does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request: Request, pk):
        try:
            non_teaching_staff = NonTeachingStaff.objects.get(pk=pk)
            serializer = NonTeachingStaffSerializer(non_teaching_staff, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                response = {
                    "status": "success",
                    "message": "Non teaching staff updated successfully",
                    "data": serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
        except NonTeachingStaff.DoesNotExist:
            response = {
                "status": "error",
                "message": "Non teaching staff does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request: Request, pk):
        try:
            non_teaching_staff = NonTeachingStaff.objects.get(pk=pk)
            non_teaching_staff.delete()
            response = {
                "status": "success",
                "message": "Non teaching staff deleted successfully"
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        except NonTeachingStaff.DoesNotExist:
            response = {
                "status": "error",
                "message": "Non teaching staff does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
