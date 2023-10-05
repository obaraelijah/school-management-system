# Generated by Django 4.2.5 on 2023-09-18 00:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("student_module", "0003_alter_student_student_id_number"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentGrade",
            fields=[
                (
                    "student_grade_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("grade", models.CharField(max_length=255)),
                ("grade_file", models.FileField(upload_to="student_grades")),
                ("grade_remark", models.CharField(max_length=255)),
                ("grade_level", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="SubmitAssignment",
            fields=[
                (
                    "submit_assignment_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "submit_assignment_file",
                    models.FileField(upload_to="submit_assignments"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name="student",
            name="student_id_number",
            field=models.CharField(default="508b4d", max_length=255),
        ),
    ]