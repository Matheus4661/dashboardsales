from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.urls import *
from escritorio.urls import *

urlpatterns = [
    path('', include('core.urls')),
    path('accounts/' ,  include ( 'django.contrib.auth.urls' )),
    path('escritorio/', include('escritorio.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    