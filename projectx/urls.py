from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django_email_verification import urls as email_urls
from projectx import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('auth/', include(('authentication.urls', 'authentication'), namespace='authentication')),
    path('email/', include(email_urls), name='email-verification'),
    path('accounts/', include('allauth.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
