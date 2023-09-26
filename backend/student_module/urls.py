from django.urls import path
from .views import (CreateListStudentView, RetrieveUpdateDestroyStudentView,
                    CreateStudentSubmittedAssignment, RetrieveUpdateDestroyStudentSubmittedAssignment,
                    CreateStudentAttendance, RetrieveUpdateDestroyStudentAttendance,
                    CreateStudentGrade, RetrieveUpdateDestroyStudentGrade,
                    AssignDepartmentForStudent, AssignTeacherForStudent, AssignCourseForStudent,)


urlpatterns = [
    path("students/", CreateListStudentView.as_view(), name="create-list-student"),
    path("students/<str:pk>/", RetrieveUpdateDestroyStudentView.as_view(), name="retrieve-update-destroy-student"),
    path("students/<str:pk>/submit-assignments/", CreateStudentSubmittedAssignment.as_view(), name="create-student-submit-assignment"),
    path("students/<str:pk>/submit-assignments/<str:submit_assignment_id>/", RetrieveUpdateDestroyStudentSubmittedAssignment.as_view(), name="retrieve-update-destroy-student-submit-assignment"),
    path("students/<str:pk>/attendances/", CreateStudentAttendance.as_view(), name="create-student-attendance"),
    path("students/<str:pk>/attendances/<str:attendance_id>/", RetrieveUpdateDestroyStudentAttendance.as_view(), name="retrieve-update-destroy-student-attendance"),
    path("students/<str:pk>/grades/", CreateStudentGrade.as_view(), name="create-student-grade"),
    path("students/<str:pk>/grades/<str:student_grade_id>/", RetrieveUpdateDestroyStudentGrade.as_view(), name="retrieve-update-destroy-student-grade"),
    path("students/<str:pk>/assign-department/", AssignDepartmentForStudent.as_view(), name="assign-department-for-student"),
    path("students/<str:pk>/assign-teacher/", AssignTeacherForStudent.as_view(), name="assign-teacher-for-student"),
    path("students/<str:pk>/assign-course/", AssignCourseForStudent.as_view(), name="assign-course-for-student"),
]