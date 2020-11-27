from django.contrib import admin
from .models import Post, Newsletter, School, SchoolClasse, Teacher, Parent, Student, Subject, StudentAndSubject, CTSS, User

admin.site.register(Post)
admin.site.register(Newsletter)
admin.site.register(School)
admin.site.register(SchoolClasse)
admin.site.register(Subject)
admin.site.register(StudentAndSubject)
admin.site.register(CTSS)
admin.site.register(User)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date',)
    ordering = ('birth_date',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date',)
    ordering = ('birth_date',)

@admin.register(Parent)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'student')
    ordering = ('birth_date',)

'''@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'type')
    ordering = ('birth_date',)
    '''


