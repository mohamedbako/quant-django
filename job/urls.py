from django.contrib import admin
from django.urls import path , include
from . import views

app_name = 'job' # name of app

urlpatterns = [
    path('' , views.jobList),
    path('<str:slug>', views.jobDetail, name='jobDetail'),
    path('Applyjob/<str:slug>/', views.jobApply,name='jobApply'),
]
