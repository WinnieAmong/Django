from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

def index2(request):
    return render(request,'myfolder/index2.html')


def about_us2(request):
    return render(request,'myfolder/about_us2.html')



# Create your views here.
