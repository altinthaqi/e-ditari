from django.db import models
from django.utils import timezone

class Newsletter(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    date_subscribed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    
