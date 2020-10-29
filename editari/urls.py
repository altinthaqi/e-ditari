from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('staff-register', views.staff_register, name='staff-register'),
    path('parent-register', views.parent_register, name='parent-register'),
    path('student-register', views.student_register, name='student-register'),
]