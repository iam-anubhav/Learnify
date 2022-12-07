from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

def aboutus(request):
    return render(request,'aboutus.html')