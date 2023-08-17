from django.contrib import admin
from .models import PromotionCategory, Promotion, NewsletterSub


@admin.register(PromotionCategory)
class PromotionCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['name', 'slug']


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'is_published']
    list_display_links = ['name', 'slug']
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(NewsletterSub)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
