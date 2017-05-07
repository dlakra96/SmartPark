from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^society_members/main/',views.manage)
]
