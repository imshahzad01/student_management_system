from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from Student_Management_App.models import CustomUser, Teachers, Classes, Subjects, Students
# from .forms import AddStudentForm, EditStudentForm


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
    return render(request, "Admin_template/add_teacher.html")


def add_teacher_save(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        print(address)

        try:
            user = Teachers.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
            user.teachers.address = address
            user.save()
            print(user)
            # Making another enrty to customuser to allow teachers login
            user1 = CustomUser.objects.create(user_type=2, username=username, password=password)
            user1.save()
            messages.success(request, "Successfully Saved!")
            return redirect('add_staff')
        except:
            messages.error(request, "Failed to Add Teachers!")
            return redirect('admin_home')



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
    return render(request, "Admin_template/edit_teachers.html", context)


def edit_teacher_save(request):
    if request.method == "POST":
        teacher_id = request.POST.get('teacher_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.get(id=teacher_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            teacher = Teachers.objects.get(admin=teacher_id)
            teacher.address = address
            teacher.save()

            messages.success(request, "Successfully Updated.")
            return redirect('/edit_teacher/' + teacher_id)

        except:
            messages.error(request, "Failed to Update Staff.")
            return redirect('/edit_staff/' + teacher_id)


def delete_teacher(request, teacher_id):
    teacher = Teachers.objects.get(admin=teacher_id)
    try:
        teacher.delete()
        messages.success(request, "Teacher Deleted Successfully.")
        return redirect('manage_teacher')
    except:
        messages.error(request, "Failed to Delete Teacher.")
        return redirect('manage_teacher')

