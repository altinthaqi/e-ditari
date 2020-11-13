from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import format_html
from django.urls import reverse

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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    birth_date = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=10)
    is_online = models.BooleanField(default=False)
    list_display = (user, birth_date, type, is_online)

    # Resize avatar image to 300x300
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


#class School(models.Model):


#class Shool_Class(models.model):


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
