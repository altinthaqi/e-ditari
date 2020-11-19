from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('staff-register', views.staff_register, name='staff-register'),
    path('parent-register', views.parent_register, name='parent-register'),
    path('student-register', views.student_register, name='student-register'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('home', PostListView.as_view(), name='blogs'),
    path('login', views.login_user, name = 'login'),
]