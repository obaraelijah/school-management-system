# Generated by Django 4.2.5 on 2023-09-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student_module", "0009_remove_student_teacher_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="student_id_number",
            field=models.CharField(default="f75ab1", max_length=255),
        ),
    ]