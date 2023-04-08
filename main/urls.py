from django.urls import path , include
from . import views

app_name = 'job' # name of app

urlpatterns = [
    path('' , views.main),
]
