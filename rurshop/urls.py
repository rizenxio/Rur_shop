from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('item/', include('item.urls')),
    path('inbox/', include('conversation.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
