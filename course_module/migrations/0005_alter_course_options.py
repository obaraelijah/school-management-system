# Generated by Django 4.2.5 on 2023-09-28 08:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("course_module", "0004_rename_department_course_departments_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course",
            options={"ordering": ["course_name"]},
        ),
    ]