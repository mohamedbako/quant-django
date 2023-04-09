from django.urls import path , include
from . import views

app_name = 'main' # name of app

urlpatterns = [
    path('' , views.main, name="main"),
]
