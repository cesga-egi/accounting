"""accounting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from accounting import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.main_view),
    url(r'^/', views.main_view),
    url(r'^discipline/$', views.discipline_view),
    #url(r'^discipline/(?P<discipline>.*?)/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/(?P<VOGroup>[\w]+)/(?P<localJobGroup>[\w]+)$', views.discipline_view),
    #url(r'^discipline/(?P<discipline>[^/]*?)/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/(?P<VOGroup>[\w]+)/$', views.discipline_view),
    #url(r'^discipline/(?P<discipline>[^/]*?)/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/$', views.discipline_view),
    #url(r'^discipline/(?P<discipline>[^/]*?)/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/$', views.discipline_view),
    #url(r'^discipline/(?P<discipline>[^/]*?)/(?P<query>[\w]+)/$', views.discipline_view),
    url(r'^discipline/(?P<discipline>[^/]*?)/$', views.discipline_view),

    url(r'^egi/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/(?P<VOGroup>[\w]+)/(?P<localJobGroup>[\w]+)/$', views.egi_view),
    url(r'^egi/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/(?P<VOGroup>[\w]+)/$', views.egi_view),
    url(r'^egi/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/$', views.egi_view),
    url(r'^egi/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/$', views.egi_view),
    url(r'^egi/(?P<query>[\w]+)/$', views.egi_view),
    url(r'^egi/ngi/(?P<ngi>[\w-]+)$', views.egi_ngi_view),
    url(r'^egi/country/(?P<country>[\w-]+)$', views.egi_country_view),
    url(r'^egi/$', views.egi_view),

    url(r'^egi/(?P<site>[\w-]+)/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/(?P<VOGroup>[\w]+)/(?P<localJobGroup>[\w]+)/$', views.egi_site_view),
    url(r'^egi/site/(?P<site>[\w-]+)/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/(?P<VOGroup>[\w]+)/$', views.egi_site_view),
    url(r'^egi/site/(?P<site>[\w-]+)/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/$', views.egi_site_view),
    url(r'^egi/site/(?P<site>[\w-]+)/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/$', views.egi_site_view),
    url(r'^egi/site/(?P<site>[\w-]+)/(?P<query>[\w]+)/$', views.egi_site_view),
    url(r'^egi/site/(?P<site>[\w-]+)$', views.egi_site_view),

    url(r'^user_dn/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/(?P<VOGroup>[\w]+)/(?P<localJobGroup>[\w]+)/$', views.user_dn_view),
    url(r'^user_dn/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/(?P<VOGroup>[\w]+)/$', views.user_dn_view),
    url(r'^user_dn/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/$', views.user_dn_view),
    url(r'^user_dn/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/$', views.user_dn_view),
    url(r'^user_dn/(?P<query>[\w]+)/$', views.user_dn_view),
    url(r'^user_dn/$', views.user_dn_view),

    url(r'^user_dn/(?P<site>[\w-]+)/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/(?P<VOGroup>[\w]+)/(?P<localJobGroup>[\w]+)/$', views.user_dn_site_view),
    url(r'^user_dn/site/(?P<site>[\w-]+)/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/(?P<VOGroup>[\w]+)/$', views.user_dn_site_view),
    url(r'^user_dn/site/(?P<site>[\w-]+)/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/$', views.user_dn_site_view),
    url(r'^user_dn/site/(?P<site>[\w-]+)/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/$', views.user_dn_site_view),
    url(r'^user_dn/site/(?P<site>[\w-]+)/(?P<query>[\w]+)/$', views.user_dn_site_view),
    url(r'^user_dn/site/(?P<site>[\w-]+)$', views.user_dn_site_view),
    url(r'^user_dn/ngi/(?P<ngi>[\w-]+)$', views.user_dn_ngi_view),
    url(r'^user_dn/country/(?P<country>[\w-]+)$', views.user_dn_country_view),

    url(r'^cloud/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/$', views.cloud_view),
    url(r'^cloud/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/$', views.cloud_view),
    url(r'^cloud/(?P<query>[\w]+)/$', views.cloud_view),
    url(r'^cloud/$', views.cloud_view),

    url(r'^cloud/site/(?P<site>[\w-]+)/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d\d)/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d\d)/$', views.cloud_site_view),
    url(r'^cloud/site/(?P<site>[\w-]+)/(?P<query>[\w]+)/(?P<xRange>[\w]+)/(?P<yRange>[\w]+)/$', views.cloud_site_view),
    url(r'^cloud/site/(?P<site>[\w-]+)/(?P<query>[\w]+)/$', views.cloud_site_view),
    url(r'^cloud/site/(?P<site>[\w-]+)$', views.cloud_site_view),

    url(r'^cloud/ngi/(?P<ngi>[\w-]+)$', views.cloud_ngi_view),
    url(r'^cloud/country/(?P<country>[\w-]+)$', views.cloud_country_view),
]
