from django.shortcuts import render
from .models import *
from rest_framework import status, generics, serializers, viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *
# Create your views here.


class DepartmentView(viewsets.ModelViewSet):
	serializer_class = DepartmentSerializer
	queryset = Department.objects.all()

class StudentView(viewsets.ModelViewSet):
	serializer_class = StudentSerializer
	queryset = Student.objects.prefetch_related('student_departments').all()
	http_method_names = ['get', 'post', 'put', 'patch', 'delete']

	def create(self, request, *args, **kwargs):
		data = request.data
		new_student = Student(first_name = data['first_name'],last_name=data['last_name'])
		new_student.save()
		for department in data['departments']:
			department_obj = Department.objects.get(dept_id=department['dept_id'])
			new_student.departments.add(department_obj)
		serializer = self.get_serializer(new_student)

		return Response(serializer.data)

class DepartmentSTView(viewsets.ModelViewSet):
	serializer_class = DepartmentSerializer
	queryset = Department.objects.select_related().all()

	def list(self, request, *args, **kwargs):
		dept = self.queryset
		dept_list = []
		for d in dept:
			dept_list.append({d.dept_name : d.student_departments.count()})
		return Response(dept_list)



	

	



	