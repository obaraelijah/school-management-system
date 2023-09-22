from django.db import models
import uuid
from school_module.models import School
from accounts.models import CustomUser
from department_module.models import Department
from teacher_module.models import Teacher, Assignment
from course_module.models import Course



class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    student_id_number = models.CharField(max_length=255, default=str(uuid.uuid4())[:6])
    phone_number = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, blank=True)
    teachers = models.ManyToManyField(Teacher, related_name="students", blank=True, null=True)
    course = models.ManyToManyField(Course, related_name="students", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Submit_assignment(models.Model):
    submit_assignment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    submit_assignment_file = models.FileField(upload_to="submit_assignments")
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Student_grade(models.Model):
    student_grade_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    grade_file = models.FileField(upload_to="student_grades/%Y/%m/%d/", null=True, blank=True)
    grade_remark = models.CharField(max_length=255, null=True, blank=True)
    grade_level = models.CharField(max_length=255, null=True, blank=True)
    teachers = models.ManyToManyField(Teacher, related_name="grade_students", blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Student_attendance(models.Model):
    attendance_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    attendance_status = models.CharField(max_length=255)
    attendance_date = models.DateField(auto_now_add=True, null=True, blank=True)
    teachers = models.ManyToManyField(Teacher, related_name="attendance_students", blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

