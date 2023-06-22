from django.contrib import admin
from django.urls import path
from authentication.views import *

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('privacy_policy/', privacy, name='privacy'),
]

