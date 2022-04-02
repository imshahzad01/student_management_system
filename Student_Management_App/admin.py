from django.contrib import admin
from . models import *
from django.contrib.auth.admin import UserAdmin

# Registering Models
class UserModel(UserAdmin):
    list_display = ['username', 'user_type']

admin.site.register(CustomUser, UserModel)
admin.site.register(Admin)
admin.site.register(Classes)
admin.site.register(Students)
admin.site.register(Subjects)
admin.site.register(Teachers)
