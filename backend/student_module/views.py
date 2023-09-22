from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Student, Submit_assignment, Student_attendance, Student_grade
from .serializers import StudentSerializer, StudentSubmitAssignmentSerializer, StudentAttendanceSerializer, StudentGradeSerializer, AssignDepartmentForStudentSerializer, AssignTeacherForStudentSerializer, AssignCourseForStudentSerializer
from rest_framework.permissions import IsAuthenticated
from department_module.models import Department
from teacher_module.models import Teacher
from course_module.models import Course


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


class CreateStudentSubmittedAssignment(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request: Request):

        data = request.data
        serializer = StudentSubmitAssignmentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                "status": "success",
                "message": "Assignment submitted successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        bad_request_response = {
            "status": "error",
            "message": "Bad request",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDestroyStudentSubmittedAssignment(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request, pk):
        try:
            assignment = Submit_assignment.objects.get(pk=pk)
            serializer = StudentSubmitAssignmentSerializer(assignment)
            response = {
                "status": "success",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        except Submit_assignment.DoesNotExist:
            response = {
                "status": "error",
                "message": "Assignment does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request: Request, pk):
        try:
            assignment = Submit_assignment.objects.get(pk=pk)
            serializer = StudentSubmitAssignmentSerializer(assignment, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                response = {
                    "status": "success",
                    "message": "Assignment updated successfully",
                    "data": serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
        except Submit_assignment.DoesNotExist:
            response = {
                "status": "error",
                "message": "Assignment does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request: Request, pk):
        try:
            assignment = Submit_assignment.objects.get(pk=pk)
            assignment.delete()
            response = {
                "status": "success",
                "message": "Assignment deleted successfully"
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        except Submit_assignment.DoesNotExist:
            response = {
                "status": "error",
                "message": "Assignment does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        

class CreateStudentAttendance(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        data = request.data
        serializer = StudentAttendanceSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                "status": "success",
                "message": "Student Attendance marked successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        bad_request_response = {
            "status": "error",
            "message": "Bad request",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
    

class RetrieveUpdateDestroyStudentAttendance(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk):
        try:
            attendance = Student_attendance.objects.get(pk=pk)
            serializer = StudentAttendanceSerializer(attendance)
            response = {
                "status": "success",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        except Student_attendance.DoesNotExist:
            response = {
                "status": "error",
                "message": "Student Attendance does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request: Request, pk):
        try:
            attendance = Student_attendance.objects.get(pk=pk)
            serializer = StudentAttendanceSerializer(attendance, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                response = {
                    "status": "success",
                    "message": "Student Attendance updated successfully",
                    "data": serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
        except Student_attendance.DoesNotExist:
            response = {
                "status": "error",
                "message": "Student Attendance does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request: Request, pk):
        try:
            attendance = Student_attendance.objects.get(pk=pk)
            attendance.delete()
            response = {
                "status": "success",
                "message": "Student Attendance deleted successfully"
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        except Student_attendance.DoesNotExist:
            response = {
                "status": "error",
                "message": "Student Attendance does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class CreateStudentGrade(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        data = request.data
        serializer = StudentGradeSerializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
            student_grade = serializer.save()

            # Calculate grade remark and level
            if student_grade.grade >= 75:
                student_grade.grade_remark = "Excellent"
                student_grade.grade_level = "A"
            elif 70 <= student_grade.grade < 75:
                student_grade.grade_remark = "Very Good"
                student_grade.grade_level = "B"
            elif 65 <= student_grade.grade < 70:
                student_grade.grade_remark = "Good"
                student_grade.grade_level = "C"
            elif 60 <= student_grade.grade < 65:
                student_grade.grade_remark = "Credit"
                student_grade.grade_level = "D"
            elif 55 <= student_grade.grade < 60:
                student_grade.grade_remark = "Pass"
                student_grade.grade_level = "E"
            else:
                student_grade.grade_remark = "Fail"
                student_grade.grade_level = "F"

            student_grade.save()  

            response = {
                "status": "success",
                "message": "Student Grade created successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)

        bad_request_response = {
            "status": "error",
            "message": "Bad request",
            "data": serializer.errors
        }
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDestroyStudentGrade(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk):
        try:
            grade = Student_grade.objects.get(pk=pk)
            serializer = StudentGradeSerializer(grade)
            response = {
                "status": "success",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        except Student_grade.DoesNotExist:
            response = {
                "status": "error",
                "message": "Student Grade does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request: Request, pk):
        try:
            grade = Student_grade.objects.get(pk=pk)
            serializer = StudentGradeSerializer(grade, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                student_grade = serializer.save()

                # Calculate grade remark and level
                if student_grade.grade >= 75:
                    student_grade.grade_remark = "Excellent"
                    student_grade.grade_level = "A"
                elif 70 <= student_grade.grade < 75:
                    student_grade.grade_remark = "Very Good"
                    student_grade.grade_level = "B"
                elif 65 <= student_grade.grade < 70:
                    student_grade.grade_remark = "Good"
                    student_grade.grade_level = "C"
                elif 60 <= student_grade.grade < 65:
                    student_grade.grade_remark = "Credit"
                    student_grade.grade_level = "D"
                elif 55 <= student_grade.grade < 60:
                    student_grade.grade_remark = "Pass"
                    student_grade.grade_level = "E"
                else:
                    student_grade.grade_remark = "Fail"
                    student_grade.grade_level = "F"

                student_grade.save()  
            
                response = {
                    "status": "success",
                    "message": "Student Grade updated successfully",
                    "data": serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
        except Student_grade.DoesNotExist:
            response = {
                "status": "error",
                "message": "Student Grade does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request: Request, pk):
        try:
            grade = Student_grade.objects.get(pk=pk)
            grade.delete()
            response = {
                "status": "success",
                "message": "Student Grade deleted successfully"
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        except Student_grade.DoesNotExist:
            response = {
                "status": "error",
                "message": "Student Grade does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class AssignDepartmentForStudent(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request: Request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = AssignDepartmentForStudentSerializer(student, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                
                try:
                    department_id = serializer.data["department_id"]
                    Department.objects.get(pk=department_id)
                except Department.DoesNotExist:
                    response = {
                        "status": "error",
                        "message": "Department does not exist"
                    }
                    return Response(response, status=status.HTTP_404_NOT_FOUND)
                
                serializer.save()

                response = {
                    "status": "success",
                    "message": "Department assigned to student successfully",
                    "data": serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
            bad_request_response = {
                "status": "error",
                "message": "Bad request",
                "data": serializer.errors
            }
            return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            response = {
                "status": "error",
                "message": "Student does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class AssignTeacherForStudent(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request: Request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = AssignTeacherForStudentSerializer(student, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                
                try:
                    teacher_id = serializer.validated_data.get("teacher_id")
                    Teacher.objects.get(pk=teacher_id)
                except Teacher.DoesNotExist:
                    response = {
                        "status": "error",
                        "message": "Teacher does not exist"
                    }
                    return Response(response, status=status.HTTP_404_NOT_FOUND)
                
                serializer.save()

                response = {
                    "status": "success",
                    "message": "Teacher assigned to student successfully",
                    "data": serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
            bad_request_response = {
                "status": "error",
                "message": "Bad request",
                "data": serializer.errors
            }
            return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            response = {
                "status": "error",
                "message": "Student does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        

class AssignCourseForStudent(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request: Request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = AssignCourseForStudentSerializer(student, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                
                try:
                    course_id = serializer.validated_data.get("course_id")
                    Course.objects.get(pk=course_id)
                except Course.DoesNotExist:
                    response = {
                        "status": "error",
                        "message": "Course does not exist"
                    }
                    return Response(response, status=status.HTTP_404_NOT_FOUND)
                
                serializer.save()

                response = {
                    "status": "success",
                    "message": "Course assigned to student successfully",
                    "data": serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
            bad_request_response = {
                "status": "error",
                "message": "Bad request",
                "data": serializer.errors
            }
            return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            response = {
                "status": "error",
                "message": "Student does not exist"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)        