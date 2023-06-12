from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('promotions/', news, name='promotions'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]

