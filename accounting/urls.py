from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('portal.urls')),
]
