# Generated by Django 3.2 on 2022-02-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='departments',
            field=models.ManyToManyField(related_name='student_departments', to='student.Department'),
        ),
    ]
