from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('feedback/', include('feedbacks.urls')),
    path('servicos/', include('servicos.urls')),
    path('pesquisas/', include('pesquisas.urls')),
    path('whatsapp/', include('botwhatsapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)