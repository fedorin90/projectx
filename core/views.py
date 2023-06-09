from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import ContactForm
from .models import Promotion, PromotionCategory


class HomeView(ListView):
    model = Promotion
    template_name = 'core/home.html'
    context_object_name = 'promotion'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

    def get_queryset(self):
        return Promotion.objects.filter(is_published=True).order_by('update')[0:6]


# def home(request):
#     return render(request, 'core/home.html', {'title': 'Home page'})

class PromotionView(ListView):
    model = Promotion
    template_name = 'core/promotions.html'
    context_object_name = 'promotion'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Promotion & discounts'
        return context

    def get_queryset(self):
        sort_by = self.request.GET.get('order_by', 'name')
        try:
            return Promotion.objects.filter(is_published=True).order_by(sort_by)
        except Exception as e:
            print(e)
            return Promotion.objects.filter(is_published=True).order_by('name')


class PromotionCategoryView(ListView):
    model = Promotion
    template_name = 'core/promotions.html'
    context_object_name = 'promotion'
    paginate_by = 6
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category: ' + str(context['promotion'][0].category)
        context['promotion_categories'] = PromotionCategory.objects.all().order_by('name')
        context['cat_selected'] = self.kwargs['slug']
        return context

    def get_queryset(self):
        return Promotion.objects.filter(category__slug=self.kwargs['slug'], is_published=True).order_by('update')


# def promotion_category(request, slug):
#     prom = Promotion.objects.filter(category__slug__contains=slug)
#     cat = PromotionCategory.objects.all()
#     context = {
#         'title': 'Promotion & discounts',
#         'promotion': prom,
#         'promotion_categories': cat,
#         'cat_selected': slug
#     }
#     return render(request, 'core/promotions.html', context=context)


class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'core/detail.html'
    context_object_name = 'promotion'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detail: ' + str(context['promotion'].name)
        return context

    def get_queryset(self):
        return Promotion.objects.filter(slug=self.kwargs['slug'], is_published=True).order_by('name')


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'core/contact.html'
    success_url = reverse_lazy('core:home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        return context

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS,
                             "Message sent successfully!")
        return HttpResponseRedirect(self.get_success_url())

    def form_valid_(self, form):
        # This method is called when valid form data has been POSTed.
        # send message from email
        subject = "Website contact"
        body = {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'email': form.cleaned_data['email'],
            'message': form.cleaned_data['message'],
        }
        message = "\n".join(body.values())

        try:
            send_mail(subject, message, 'myr.devel@gmail.com', ['myr.devel@gmail.com'])
            # messages.add_message(self.request, messages.SUCCESS,
            #                      "Message sent successfully!")
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return super().form_valid(form)


def about(request):
    return render(request, 'core/about.html', {'title': 'About'})

