from django.shortcuts import render, get_object_or_404
from .models import Promotion, PromotionCategory, PromotionImage


def home(request):
    return render(request, 'core/home.html', {'title': 'Home page'})


def promotion(request):
    prom = Promotion.objects.all()
    cat = PromotionCategory.objects.all()
    context = {
        'title': 'Promotion & discounts',
        'promotion': prom,
        'promotion_categories': cat
    }
    return render(request, 'core/promotions.html', context=context)


def promotion_category(request, slug):
    prom = Promotion.objects.filter(category__slug__contains=slug)
    cat = PromotionCategory.objects.all()
    context = {
        'title': 'Promotion & discounts',
        'promotion': prom,
        'promotion_categories': cat,
        'cat_selected': slug
    }
    return render(request, 'core/promotions.html', context=context)


def promotion_detail(request, slug):
    prom = get_object_or_404(Promotion, slug=slug)
    context = {
        'title': 'Promotion detail',
        'promotion': prom,
        'cat_selected': slug
    }
    return render(request, 'core/detail.html', context=context)


def contact(request):
    return render(request, 'core/contact.html', {'title': 'Contact'})


def about(request):
    return render(request, 'core/about.html', {'title': 'About'})

