# from channels.auth import login, logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from Student_Management_App.EmailBackEnd import EmailBackEnd
from Student_Management_App.models import CustomUser


def home(request):
    return render(request, 'index.html')


def loginPage(request):
    return render(request, 'login_page.html')


def login(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        print(user)
        if user != None:
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_home')
                
            elif user_type == '2':
                return redirect('manage_teacher')
            else:
                messages.error(request, "Something went wrong!")
                return redirect('login')
        else:
            messages.error(request, "Wrong Credentials!")
            return redirect('login')

