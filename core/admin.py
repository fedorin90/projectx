from django.contrib import admin
from .models import PromotionCategory, Promotion


class PromotionCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['name', 'slug']
    search_fields = ('name',)

    class Meta:
        verbose_name = 'Promotions category'
        verbose_name_plural = 'Promotions categories'


admin.site.register(PromotionCategory, PromotionCategoryAdmin)


class PromotionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'create', 'update', 'image']
    list_display_links = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
    list_filter = ('name', 'create', 'update')

    class Meta:
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'
        ordering = [
            'update',
            'title'
                    ]


admin.site.register(Promotion, PromotionAdmin)
