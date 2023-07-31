from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request,'myfolder/index.html')


def about_us(request):
    return render(request,'myfolder/about_us.html')






# Create your views here.
