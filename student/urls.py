from . import views
# from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('department', views.DepartmentView, basename='department_api')
router.register('department_st', views.DepartmentSTView, basename='department_st_api')
router.register('student', views.StudentView, basename='student_api')


urlpatterns = [
]
