from django.http import HttpResponse
from django.shortcuts import render,redirect
from Users.models import UserData
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        details = [name,email,password]
        if '' in details:
            messages.success(request, "Some field is empty")
            return redirect('/signup')
        elif '@' not in email:
            messages.success(request, "Invalid Email")
            return redirect('/signup')
        elif password != confirm:
            messages.success(request,"Password do not matched")
            return redirect('/signup')
        else:
            data = UserData(name=name,email=email, password=password)
            data.save()
            messages.success(request, "You are registered. Sign in now")
            return redirect('/signup')

    return render(request,'signup.html')

def subjects(request):
    return render(request,'subjects.html')

def singlesubject(request):
    return render(request,'single-subject.html')

def topic(request):
    return render(request,'topic.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')