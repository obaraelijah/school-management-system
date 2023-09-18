from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated


class CreateListStudentView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        response = {
            "status": "success",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                "status": "success",
                "message": "Student created successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        bad_request_response = {
            "status": "error",
            "message": "Bad request",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
    

class RetrieveUpdateDestroyStudentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            response = {
                "status": "success",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            response = {
                "status": "error",
                "message": "Student does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request: Request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                response = {
                    "status": "success",
                    "message": "Student updated successfully",
                    "data": serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            response = {
                "status": "error",
                "message": "Student does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request: Request, pk):
        try:
            student = Student.objects.get(pk=pk)
            student.delete()
            response = {
                "status": "success",
                "message": "Student deleted successfully"
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            response = {
                "status": "error",
                "message": "Student does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
    
