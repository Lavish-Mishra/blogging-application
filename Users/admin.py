from django.contrib import admin
#from django.contrib.auth.models import User
from .models import profile, CustomUser

# Register your models here.
admin.site.register(CustomUser)

@admin.register(profile)
class ProfileAdmin(admin.ModelAdmin):
    #list_display = ('user',)
    pass