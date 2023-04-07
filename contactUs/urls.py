from django.contrib import admin
from django.urls import path , include
from . import views

app_name = 'contactUs' # name of app

urlpatterns = [
    path('' , views.sendMessage),
]
