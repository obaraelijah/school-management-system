from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request


class CreateListCourse(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        response = {
            "status": "success",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request: Request):
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

    def get(self, request: Request, pk):
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
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def put(self, request: Request, pk):
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
    
    def delete(self, request: Request, pk):
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
