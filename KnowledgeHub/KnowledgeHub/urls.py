from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import include, path

urlpatterns = [
    path('member/', include('member.urls')),
    path('exam/', include('examination.urls')),
    path('', include('theblog.urls')),
    path('messenger/', include('messenger.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
