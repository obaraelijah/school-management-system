# Generated by Django 4.2.5 on 2023-09-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student_module", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="student_id_number",
            field=models.CharField(default="bfede7", max_length=255),
        ),
    ]