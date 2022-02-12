from rest_framework import serializers
from .models import *
# from itertools import groupby
# from django.core.files.storage import default_storage
# from django.db.models import Q
from rest_framework.response import Response
# import json

class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
	full_name = serializers.SerializerMethodField('get_full_name', read_only=True)
	
	class Meta:
		model = Student
		fields = '__all__'
		depth = 1 
	

	def get_full_name(self, obj):
		return obj.first_name + " "+ obj.last_name
	
		
	