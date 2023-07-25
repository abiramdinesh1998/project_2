from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_3(request):
    return render(request,'text5.html')

def second_3(request):
    return render(request,'text6.html')

def third_3(request):
    return HttpResponse('<h1>captian amarica</h1>')


