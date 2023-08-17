from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import ContactForm, NewsletterSubForm
from .models import Promotion, PromotionCategory, NewsletterSub
from .tasks import contact_info_tusk


class HomeView(ListView, FormView):
    model = [Promotion, NewsletterSub]
    template_name = 'core/home.html'
    context_object_name = 'promotion'
    form_class = NewsletterSubForm
    success_url = reverse_lazy('core:home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

    def get_queryset(self):
        return Promotion.objects.filter(is_published=True).order_by('updated_at')[0:6]

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # send message from email
        subject = "NewsLetter"
        body = {
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email']
        }
        message = "Hello. You subscribed to the newsletter we will send you a lot of spam here"

        try:
            NewsletterSub.objects.create(name=body['name'], email=body['email'])
            send_mail(subject, message, 'fedorin.mir@gamil.com', [form.cleaned_data['email']])
            messages.add_message(self.request, messages.SUCCESS,
                                 "Message sent successfully!")
        except BadHeaderError:

            messages.add_message(self.request, messages.ERROR,
                                 "Error sending message")
            return HttpResponseRedirect(self.get_success_url())
        except IntegrityError:
            messages.add_message(self.request, messages.INFO,
                                 "You already subscribe")
            return HttpResponseRedirect(self.get_success_url())
        return super().form_valid(form)


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
        return Promotion.objects.filter(category__slug=self.kwargs['slug'], is_published=True).order_by('updated_at')


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
        # This method is called when valid form data has been POSTed.
        # send message from email
        contact_info_tusk.delay(
            form.cleaned_data['first_name'],
            form.cleaned_data['last_name'],
            form.cleaned_data['email'],
            form.cleaned_data['message'])
        messages.add_message(self.request, messages.SUCCESS,
                             "Message sent successfully!")
        return super().form_valid(form)


def about(request):
    return render(request, 'core/about.html', {'title': 'About'})

