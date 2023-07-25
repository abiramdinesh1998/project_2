from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_1(request):
    return render(request,'text1.html')

def second_1(request):
    return render(request,'text2.html')

def third_1(request):
    return HttpResponse('<h1>avengers</h1>')

