# Generated by Django 4.2.5 on 2023-09-22 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("course_module", "0003_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("teacher_module", "0001_initial"),
        ("department_module", "0001_initial"),
        ("school_module", "0001_initial"),
        ("student_module", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="submit_assignment",
            name="assignment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="teacher_module.assignment",
            ),
        ),
        migrations.AddField(
            model_name="submit_assignment",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="school_module.school"
            ),
        ),
        migrations.AddField(
            model_name="submit_assignment",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="student_module.student"
            ),
        ),
        migrations.AddField(
            model_name="student_grade",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="course_module.course"
            ),
        ),
        migrations.AddField(
            model_name="student_grade",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="school_module.school"
            ),
        ),
        migrations.AddField(
            model_name="student_grade",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="student_module.student"
            ),
        ),
        migrations.AddField(
            model_name="student_grade",
            name="teachers",
            field=models.ManyToManyField(
                blank=True, related_name="grade_students", to="teacher_module.teacher"
            ),
        ),
        migrations.AddField(
            model_name="student_attendance",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="course_module.course"
            ),
        ),
        migrations.AddField(
            model_name="student_attendance",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="school_module.school"
            ),
        ),
        migrations.AddField(
            model_name="student_attendance",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="student_module.student"
            ),
        ),
        migrations.AddField(
            model_name="student_attendance",
            name="teachers",
            field=models.ManyToManyField(
                blank=True,
                related_name="attendance_students",
                to="teacher_module.teacher",
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="course",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="students",
                to="course_module.course",
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="department_module.department",
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="school_module.school"
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="teachers",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="students",
                to="teacher_module.teacher",
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
