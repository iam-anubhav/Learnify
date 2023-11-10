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

def seven(request):
    return render(request,'7th.html')
def eight(request):
    return render(request,'8th.html')
def nine(request):
    return render(request,'9th.html')
def ten(request):
    return render(request,'10th.html')
def eleven(request):
    return render(request,'11th.html')
def twelve(request):
    return render(request,'12th.html')
def singlesubject(request):
    return render(request,'single-subject.html')
def science(request):
    return render(request,'science.html')
def hindi(request):
    return render(request,'hindi.html')
def english(request):
    return render(request,'english.html')
def sst(request):
    return render(request,'sst.html')

def topic(request):
    return render(request,'topic.html')
def th(request):
    return render(request,'th.html')
def te(request):
    return render(request,'te.html')
def ts(request):
    return render(request,'ts.html')
def tss(request):
    return render(request,'tss.html')
def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')