from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_2(request):
    return render(request,'text3.html')

def second_2(request):
    return render(request,'text4.html')

def third_2(request):
    return HttpResponse('<h1>iron man</h1>')

