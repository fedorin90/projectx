from django.contrib import admin
from .models import PromotionCategory, Promotion


class PromotionCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['name', 'slug']


admin.site.register(PromotionCategory, PromotionCategoryAdmin)


class PromotionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'is_published']
    list_display_links = ['name', 'slug']
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Promotion, PromotionAdmin)
