from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('cart/', include('cart.urls')),
    path('profile/', include('profile.urls')),
    path('api/', include('api.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

