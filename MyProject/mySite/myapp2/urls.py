from django.urls import path
#lets import views file from 'myapp' Application
from myapp2 import views 
urlpatterns=[
    path('index2/',views.index2,name='index2'), 
    path('about2/',views.about_us2,name='about_us2')  
]