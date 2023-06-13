from django.contrib import admin
from .models import PromotionCategory, Promotion


class PromotionCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['name', 'slug']
    search_fields = ('name',)


admin.site.register(PromotionCategory, PromotionCategoryAdmin)


class PromotionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_display_links = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Promotion, PromotionAdmin)
