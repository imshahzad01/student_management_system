from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    return render(request, 'base.html')