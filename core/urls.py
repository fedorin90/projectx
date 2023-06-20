from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('promotions/', PromotionView.as_view(), name='promotions'),
    path('promotions/category/<slug:slug>/', PromotionCategoryView.as_view(), name='promotion_category'),
    path('promotions/detail/<slug:slug>/', PromotionDetailView.as_view(), name='promotion_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', about, name='about'),
]

