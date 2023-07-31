from django.urls import path
#lets import views file from 'president application'Application
from presidentApp import views
urlpatterns=[
    path('presdo',views.presdo,name='presdo'),

]