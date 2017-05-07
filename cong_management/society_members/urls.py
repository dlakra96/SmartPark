from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf.urls.static import settings
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^society_members/main/',views.number_search),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
