from django.shortcuts import render
from .models import Promotion, PromotionCategory, PromotionImage


def home(request):
    return render(request, 'core/home.html', {'title': 'Home page'})


def promotion(request):
    prom = Promotion.objects.all()
    cat = PromotionCategory.objects.all()
    return render(request, 'core/promotions.html', {
        'title': 'Promotion & discounts', 'promotion': prom, 'promotion_categories': cat})


def promotion_category(request):
    return render(request, 'core/home.html', {'title': 'Promotion category'})


def promotion_detail(request):
    return render(request, 'core/home.html', {'title': 'Promotion detail'})



def contact(request):
    return render(request, 'core/contact.html', {'title': 'Contact'})


def about(request):
    return render(request, 'core/about.html', {'title': 'About'})

