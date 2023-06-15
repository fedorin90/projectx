from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('promotions/', promotion, name='promotions'),
    path('promotions/category/<str:slug>/', promotion_category, name='promotion_category'),
    path('promotions/detail/<str:slug>/', promotion_detail, name='promotion_detail'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]

