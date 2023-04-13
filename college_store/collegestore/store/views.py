from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def index(request):
    return render(request,'index.html')
def courses(request):
    return render(request,'courses.html')
def new(request):

    return render(request,'new.html')

