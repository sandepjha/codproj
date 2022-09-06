from django.contrib import admin
from .models import Post, UserProfile
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['body']


admin.site.register(UserProfile)