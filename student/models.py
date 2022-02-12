from django.db import models

# Create your models here.

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    dept_head = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Departments'

class Student(models.Model): 
    std_id =models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    departments = models.ManyToManyField("Department",related_name="student_departments")

    class Meta:
        verbose_name_plural = 'Students'

