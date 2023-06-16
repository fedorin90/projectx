from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('promotions/', promotion, name='promotions'),
    path('promotions/category/<slug:slug>/', promotion_category, name='promotion_category'),
    path('promotions/detail/<slug:slug>/', promotion_detail, name='promotion_detail'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]

