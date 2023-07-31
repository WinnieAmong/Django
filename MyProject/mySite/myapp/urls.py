from django.urls import path
#lets import views file from 'myapp' Application
from myapp import views 
urlpatterns=[
    path('index/',views.index,name='index'), 
    path('about/',views.about_us,name='about_us')  
]

