from django.conf.urls import include,url
from django.contrib import admin
from . import views
from  django.conf import settings
from  django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^society_members/main/', include('society_members.urls')),
    url(r'^$', include('society_members.urls')),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
