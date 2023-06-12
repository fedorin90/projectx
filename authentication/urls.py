from django.contrib import admin
from django.urls import path
from authentication.views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', login, name='register'),
]

