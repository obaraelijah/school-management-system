from rest_framework import serializers
from .models import Student, Submit_assignment, Student_grade, Student_attendance
from department_module.models import Department
from course_module.models import Course
from school_module.models import School
from accounts.models import CustomUser
from teacher_module.models import Teacher


class StudentSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField()
    user_first_name = serializers.CharField(source="user.first_name", read_only=True)
    user_last_name = serializers.CharField(source="user.last_name", read_only=True)
    school_id = serializers.UUIDField()
    school_name = serializers.CharField(source="school.school_name", read_only=True)
    department_id = serializers.UUIDField()
    department_name = serializers.CharField(source="department.department_name", read_only=True)
    courses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True, read_only=True)
    teachers = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), many=True, read_only=True)
    
    class Meta:
        model = Student
        fields = [
            "student_id",
            "student_id_number",
            "phone_number",
            "date_of_birth",
            "gender",
            "street_address",
            "city",
            "state",
            "country",
            "school_id",
            "school_name",
            "user_id",
            "user_first_name",
            "user_last_name",
            "department_id",
            "department_name",
            "courses",
            "teachers",
         ]


class StudentSubmitAssignmentSerializer(serializers.ModelSerializer):
    school_id = serializers.UUIDField()
    assignment_id = serializers.UUIDField()
    student_id = serializers.UUIDField()

    class Meta:
        model = Submit_assignment
        fields = ["school_id",
                  "assignment_id",
                  "student_id",
                  "submit_assignment_id",
                  "submit_assignment_file",
                
                  ]


class StudentAttendanceSerializer(serializers.ModelSerializer):
    school_id = serializers.UUIDField()
    student_id = serializers.UUIDField()
    teacher_id = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), many=True)
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)

    class Meta:
        model = Student_attendance
        fields = ["school_id",
                  "student_id",
                  "course_id",
                  "teacher_id",
                  "attendance_id",
                  "attendance_status",
                  "attendance_date",
                  ]


class StudentGradeSerializer(serializers.ModelSerializer):
    school_id = serializers.UUIDField()
    student_id = serializers.UUIDField()
    teacher_id = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), many=True)
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)

    class Meta:
        model = Student_grade
        fields = ["school_id",
                  "student_id",
                  "course_id",
                  "teacher_id",
                  "student_grade_id",
                  "grade",
                  "grade_file",
                  "grade_remark",
                  "grade_level",
                  ]
    

class AssignDepartmentForStudentSerializer(serializers.ModelSerializer):
    school_id = serializers.UUIDField()
    student_id = serializers.UUIDField()
    department_id = serializers.UUIDField()
    department_name = serializers.CharField(source="department.department_name", read_only=True)

    class Meta:
        model = Student
        fields = ["school_id",
                  "student_id",
                  "department_id",
                  "department_name",
                  ]


class AssignCourseForStudentSerializer(serializers.ModelSerializer):
    school_id = serializers.UUIDField()
    student_id = serializers.UUIDField()
    courses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)

    class Meta:
        model = Student
        fields = ["school_id",
                  "student_id",
                  "courses"
                  ]
    

class AssignTeacherForStudentSerializer(serializers.ModelSerializer):
    school_id = serializers.UUIDField()
    student_id = serializers.UUIDField()
    student_first_name = serializers.CharField(source="user.first_name", read_only=True)
    student_last_name = serializers.CharField(source="user.last_name", read_only=True)
    teachers = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), many=True)
    # teacher_name = serializers.CharField(source="teacher.teacher_name", read_only=True)

    class Meta:
        model = Student
        fields = ["school_id",
                  "student_id",
                  "student_first_name",
                  "student_last_name",
                  "teachers",
                  ]