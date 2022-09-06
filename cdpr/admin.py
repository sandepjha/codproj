from django.contrib import admin
from cdpr.models import Register
# Register your models here.

@admin.register(Register)
class SignupAdmin(admin.ModelAdmin):
    list_display = ['name','mobile','email','password']