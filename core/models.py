from django.core.files import File
from django.db import models
from django.urls import reverse


class PromotionCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('core:promotion_category', args=[self.slug])

    def __str__(self):
        return self.name


class Promotion(models.Model):
    category = models.ForeignKey('PromotionCategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to="photos/%Y/%m/%d/", blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('core:promotion_detail', args=[self.slug])

    def __str__(self):
        return self.name


# class PromotionImage(models.Model):
#     promotion = models.ForeignKey('Promotion', default=None, on_delete=models.CASCADE)
#     image = models.FileField(upload_to='photos/%Y/%m/%d', blank=True)
#
#     def __str__(self):
#         return self.promotion.name
#
# count = 0
# for i in range(10000):
#     count += 1
#     m = Promotion(category_id=random.randint(1, 3), name=f'promotion: {count}', slug=f'promotion{count}', description=f'{"description " * 20}')
#     m.image.save('Pr.jpg', File(open('/home/fed/Завантаження/pra.jpg', 'rb')))
#     m.save()
#
