from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher, Assignment
# from student_module.models import Submit_assignment
from .serializers import TeacherSerializer, AssignmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request


class CreateListTeacher(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        data = request.data
        serializer = TeacherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "Teacher Created Successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        bad_request_response = {
            "status": "failed",
            "message": "Teacher Creation Failed",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request: Request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        response = {
            "status": "success",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
        

class RetrieveUpdateDeleteTeacher(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            error_response = {
                "status": "failed",
                "message": "Teacher not found"
            }
            return Response(error_response, status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherSerializer(teacher)
        response = {
            "status": "success",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def put(self, request: Request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            error_response = {
                "status": "failed",
                "message": "Teacher not found"
            }
            return Response(error_response, status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherSerializer(teacher, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "Teacher Updated Successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        bad_request_response = {
            "status": "failed",
            "message": "Teacher Update Failed",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            error_response = {
                "status": "failed",
                "message": "Teacher not found"
            }
            return Response(error_response, status=status.HTTP_404_NOT_FOUND)
        teacher.delete()
        response = {
            "status": "success",
            "message": "Teacher Deleted Successfully"
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)


class CreateListAssignmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        response = {
            "status": "success",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def post(self, request: Request):
        data = request.data
        serializer = AssignmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "Assignment created succesfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        bad_request_response = {
            "status": "bad request",
            "message": "Assignment not created",
            "error_message": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDeleteAssignmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk):
        try:
            assignment = Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist:
            error_response = {
                "status": "failed",
                "message": "Assignment not found"
            }
            return Response(error_response, status=status.HTTP_404_NOT_FOUND)
        serializer = AssignmentSerializer(assignment)
        response = {
            "status": "success",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def put(self, request: Request, pk):
        try:
            assignment = Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist:
            error_response = {
                "status": "failed",
                "message": "Assignment not found"
            }
            return Response(error_response, status=status.HTTP_404_NOT_FOUND)
        serializer = AssignmentSerializer(assignment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "Assignment Updated Successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        bad_request_response = {
            "status": "failed",
            "message": "Assignment Update Failed",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk):
        try:
            assignment = Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist:
            error_response = {
                "status": "failed",
                "message": "Assignment not found"
            }
            return Response(error_response, status=status.HTTP_404_NOT_FOUND)
        assignment.delete()
        response = {
            "status": "success",
            "message": "Assignment Deleted Successfully"
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)



