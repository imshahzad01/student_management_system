from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from Student_Management_App.models import User, Teachers, Classes, Subjects, Students
from .forms import AddStudentForm, EditStudentForm


def admin_home(request):
    all_student_count = Students.objects.all().count()
    subject_count = Subjects.objects.all().count()
    classe_count = Classes.objects.all().count()
    teacher_count = Teachers.objects.all().count()

    
    all_student = Students.objects.all()
    subjects = Subjects.objects.all()
    classes = Classes.objects.all()
    teachers = Teachers.objects.all()

    context={
        "all_student_count": all_student_count,
        "subject_count": subject_count,
        "classe_count": classe_count,
        "teacher_count": teacher_count,
    }
    return render(request, "Admin_template/home.html", context)


def add_teacher(request):
    return render(request, "Admin_template/add_staff_template.html")


def add_teacher_save(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.staffs.address = address
            user.save()
            messages.success(request, "Added Successfully!")
            return redirect('add_staff')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('add_teachers')



def manage_teacher(request):
    teachers = Teachers.objects.all()
    context = {
        "teachers": teachers
    }
    return render(request, "Admin_template/manage_teachers.html", context)


def edit_teacher(request, teacher_id):
    teacher = Teachers.objects.get(admin=teacher_id)

    context = {
        "teacher": teacher,
        "id": teacher_id
    }
    return render(request, "Admin_template/edit_staff_template.html", context)


def edit_teacher_save(request):
    if request.method == "POST":
        teacher_id = request.POST.get('teacher_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        try:
            user = User.objects.get(id=teacher_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            staff_model = Teachers.objects.get(admin=teacher_id)
            staff_model.address = address
            staff_model.save()

            messages.success(request, "Successfully Updated.")
            return redirect('/edit_staff/' + teacher_id)

        except:
            messages.error(request, "Failed to Update Staff.")
            return redirect('/edit_staff/' + teacher_id)


