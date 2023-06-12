from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'core/home.html', {'title': 'Home page'})


def news(request):
    return render(request, 'core/promotions.html', {'title': 'News'})


def contact(request):
    return render(request, 'core/contact.html', {'title': 'Contact'})


def about(request):
    return render(request, 'core/about.html', {'title': 'About'})

