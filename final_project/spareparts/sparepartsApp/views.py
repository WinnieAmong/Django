from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
def index(request):
    return render(request,'spare/index.html')

def home(request):
    return render(request,'spare/home.html')

def winnie(request):
    return render(request,'spare/winnie.html')

def home2(request):
    return render(request,'spare/home2.html')



# Create your views here.
