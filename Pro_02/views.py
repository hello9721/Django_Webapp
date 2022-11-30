#-*- coding:utf-8 -*-

from django.shortcuts import render
from .models import Me
# from django.http import HttpResponse

# Create your views here.

def intro(a):
    return render(a, 'introduce/intro.html')

def project(a):
    return render(a, 'project/project.html')

def skill(a):
    return render(a, 'skill/skill.html')

def home(a):
    return render(a, 'home/index.html')

def calculator(a):
    return render(a, 'project/toy/Calculator/Calculator.html')

def diary(a):
    lst = Me.objects.all()
    context = {'list': lst}
    return render(a, 'me/diary.html', context)