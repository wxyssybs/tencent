from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def personal_page(request):
    return render(request,'personalpage.html')


def F001(request):
    return render(request,'F001.html')


def F002(request):
    return render(request,'F002.html')


def F003(request):
    return render(request,'F003.html')


def F004(request):
    return render(request,'F004.html')


def F005(request):
    return render(request,'F005.html')


def F006(request):
    return render(request,'F006.html')


def F007(request):
    return render(request,'F007.html')


def F007_1(request):
    return render(request,'F007_1.html')


def F008(request):
    return render(request,'F008.html')