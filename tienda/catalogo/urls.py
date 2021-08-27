from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Home,name='home'),
    path('home/', Home2,name='home2'),
]
