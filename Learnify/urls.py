"""Learnify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('subjects', views.subjects, name="subjects"),
    path('7th', views.seven, name="seven"),
    path('8th', views.eight, name="eight"),
    path('9th', views.nine, name="nine"),
    path('10th', views.ten, name="ten"),
    path('11th', views.eleven, name="eleven"),
    path('12th', views.twelve, name="twelve"),
    path('hindi', views.hindi, name="hindi"),
    path('english', views.english, name="english"),
    path('sst', views.sst, name="sst"),
    path('science', views.science, name="science"),
    path('singlesubject', views.singlesubject, name="singlesubject"),
    path('topic', views.topic, name="topic"),
    path('th', views.th, name="th"),
    path('te', views.te, name="te"),
    path('ts', views.ts, name="ts"),
    path('tss', views.tss, name="tss"),
]
