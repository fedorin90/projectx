from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from projectx import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('auth/', include(('authentication.urls', 'authentication'), namespace='authentication')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
