from core.models import PromotionCategory


def promotion_categories(request):
    return {'promotion_categories': PromotionCategory.objects.all()}
