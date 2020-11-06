from django.contrib import admin
from .models import Newsletter

from .models import Post

admin.site.register(Post)
admin.site.register(Newsletter)