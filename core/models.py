import django_filters
from django.db import models
from django.urls import reverse


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PromotionCategory(TimeStampedModel):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('core:promotion_category', args=[self.slug])

    def __str__(self):
        return self.name


class Promotion(TimeStampedModel):
    category = models.ForeignKey('PromotionCategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to="photos/%Y/%m/%d/", blank=True)
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('core:promotion_detail', args=[self.slug])

    def __str__(self):
        return self.name


class PromotionFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Promotion
        fields = ['name', ]




















# for i in range(10000):
#     m = Promotion(
#     category_id=random.randint(1, 3),
#     name=f'promotion: {count}',
#     slug=f'promotion{count}',
#     description=f'{"description " * 20}'
#     )
#     m.image.save('Pr.jpg', File(open('/home/fed/Завантаження/pra.jpg', 'rb')))
#     m.save()
#
