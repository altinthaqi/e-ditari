from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
<<<<<<< HEAD
from django.utils.html import format_html
from django.urls import reverse
=======
from django.core.exceptions import ObjectDoesNotExist


class User(AbstractUser):
    #Create the user from Abstract User
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

>>>>>>> Altered Database

from PIL import Image
class Newsletter(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    date_subscribed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title    
        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class School(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class SchoolClasse(models.Model):
    class_number = models.CharField(max_length=10)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_number

    def __unicode__(self):
        return self.class_number


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='teacher')
    birth_date = models.DateField(null=True, blank=True)
    school = models.ForeignKey(School, null=True, on_delete=models.SET_NULL)
    s_class = models.ForeignKey(SchoolClasse, null=True, on_delete=models.SET_NULL)
    list_display = (user, birth_date)


class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    professor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    to_class = models.ForeignKey(SchoolClasse, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name

    def __unicode__(self):
        return self.subject_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='student')
    birth_date = models.DateField(null=True, blank=True)
    school = models.ForeignKey(School, null=True, on_delete=models.SET_NULL)
    student_class = models.ForeignKey(SchoolClasse, null=True, on_delete=models.SET_NULL)
    list_display = (user, birth_date)

    def __str__(self):
        return self.user.first_name

    def __unicode__(self):
        return self.user.first_name


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='parent')
    birth_date = models.DateField(null=True, blank=True)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    list_display = (user, birth_date)


class StudentAndSubject(models.Model):
    subject_grade = models.CharField(max_length=4)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_grade

    def __unicode__(self):
        return self.subject_grade


class CTSS(models.Model):
    temp = models.CharField(max_length=4)
    the_class = models.ForeignKey(SchoolClasse, on_delete=models.CASCADE)
    professor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_subject = models.ForeignKey(StudentAndSubject, on_delete=models.CASCADE)

    def __str__(self):
        return self.temp

    def __unicode__(self):
        return self.temp


@receiver(post_save, sender=User)
<<<<<<< HEAD
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
=======
def update_profile_signal(instance, created, **kwargs):
    print("Its receiver")
    print("Student", User.is_student)
    print("Teacher", User.is_teacher)
    if User.is_teacher:
        print("Its teacher")
        try:
            instance.teacher.save()
        except ObjectDoesNotExist:
            Teacher.objects.create(user=instance)
    elif User.is_student:
        print("Its student")
        try:
            instance.student.save()
        except ObjectDoesNotExist:
            Student.objects.create(user=instance)
    else:
        print("Its parent")
        try:
            instance.parent.save()
        except ObjectDoesNotExist:
            Parent.objects.create(user=instance)
>>>>>>> Altered Database
