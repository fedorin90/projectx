from django_email_verification import urls as email_urls
from django.contrib import admin
from django.urls import path, include
from authentication.views import *

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('privacy_policy/', privacy, name='privacy'),
    path('logout/', logout_user, name='logout'),
]

