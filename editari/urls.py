from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blogs-home'),
    path('staff-login', views.staff_login, name='staff-login'),
    path('parent-login', views.parent_login, name='parent-login'),
    path('student-login', views.student_login, name='student-login'),
]