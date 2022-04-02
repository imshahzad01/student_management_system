from django.contrib import admin
from django.urls import path
from . import Admin_views, Student_views, Teachers_views 

urlpatterns = [
    path('admin_home/', Admin_views.admin_home, name="admin_home"),
    path('add_teacher/', Admin_views.add_teacher, name="add_teacher"),
    path('add_teacher_save/', Admin_views.add_staff_save, name="add_teacher_save"),
    path('manage_teacher/', Admin_views.manage_staff, name="manage_teacher"),
    path('edit_teacher/<teacher_id>/', Admin_views.edit_staff, name="edit_teacher"),
    path('edit_teacher_save/', Admin_views.edit_staff_save, name="edit_teacher_save"),
    path('delete_teacher/<teacher_id>/', Admin_views.delete_staff, name="delete_teacher"),

] 