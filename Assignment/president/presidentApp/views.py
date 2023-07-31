from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
def presdo(request):
    return render(request,'country/presdo.html')
# Create your views here.
