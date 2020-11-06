from django.contrib import admin
from .models import Newsletter, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'type')
    ordering = ('birth_date',)


admin.site.register(Newsletter)
#admin.site.register(Profile)
