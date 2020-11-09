from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('staff-register', views.staff_register, name='staff-register'),
    path('parent-register', views.parent_register, name='parent-register'),
    path('student-register', views.student_register, name='student-register'),
    path('home', views.blogs, name='blogs'),
    path('login', views.login_user, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='editari/logout.html'), name='logout'),
    path('edit-profile', views.edit_profile, name='edit-profile'),
]
