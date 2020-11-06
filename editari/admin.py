from django.contrib import admin
from .models import Newsletter, Profile

from .models import Post

admin.site.register(Post)
admin.site.register(Newsletter)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'type')
    ordering = ('birth_date',)
