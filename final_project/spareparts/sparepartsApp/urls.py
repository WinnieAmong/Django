from django.urls import path
#let us reuse the Django login view
from django.contrib.auth import views as auth_views



#lets import views file from 'myapp' Application
from sparepartsApp import views 
urlpatterns=[
    # path('',views.index,name='index'), 
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('login/',auth_views.LoginView.as_view (template_name='spare/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view (template_name='spare/index.html'),name='logout'),
    path('home2/',views.home2,name='home2'),
]
