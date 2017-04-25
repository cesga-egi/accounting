"""accounting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^(?P<format>JSON/|CSV/|)/?$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^(?P<format>JSON/|CSV/|)/?$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from accounting import views
from accounting import views_api
from accounting import settings
from accounting import rebus_tier1_views
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.main_view),
    url(r'^/', views.main_view),
    url(r'^/images/$', RedirectView.as_view(url='/static/images/')),

##### REPORTS RC API
    url(r'^report/resource_centres/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<report>[\w]+)/(?P<infra>[\w\s]+)/(?P<format>JSON|CSV)/$', views_api.report_rc),
    url(r'^report/resource_centres/(?P<format>JSON|CSV)/$', views_api.report_rc),

##### REPORTS RC
    url(r'^report/resource_centres/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<report>[\w]+)/(?P<infra>[\w\s]+)/$', views.report_rc),
    url(r'^report/resource_centres/$', views.report_rc),

##### DISCIPLINE REPORT API
    url(r'^report/disciplines/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<infra>[\w\s]+)/(?P<disciplines>[\w\W\s;]+)/(?P<format>JSON|CSV)/$', views_api.report_dis),
    url(r'^report/disciplines/(?P<format>JSON|CSV)/$', views_api.report_dis),

##### DISCIPLINE REPORT
    url(r'^report/disciplines/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<infra>[\w\s]+)/(?P<disciplines>[\w\W\s;]+)/$', views.report_dis),
    url(r'^report/disciplines/$', views.report_dis),

##### TIER2 REPORT 
    url(r'^wlcg/report/tier2/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<days>[\w]+)/(?P<format>CSV)/$', views_api.wlcg_report_tier2),
    url(r'^wlcg/report/tier2/(?P<format>CSV)/$', views_api.wlcg_report_tier2),

##### TIER2 REPORT API
    url(r'^wlcg/report/tier2/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<days>[\w]+)/$', views.wlcg_report_tier2),
    url(r'^wlcg/report/tier2/$', views.wlcg_report_tier2),

##### WLCG REPORTS COUNTRY API
    url(r'^wlcg/report/countries/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<days>[\w]+)/(?P<format>CSV)/$', views_api.wlcg_report_countries),
    url(r'^wlcg/report/countries/(?P<format>CSV)/$', views_api.wlcg_report_countries),

##### WLCG REPORTS COUNTRY API
    url(r'^wlcg/report/countries/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<days>[\w]+)/$', views.wlcg_report_countries),
    url(r'^wlcg/report/countries/$', views.wlcg_report_countries),

##### REBUS TIER1 REPORT
    url(r'^wlcg/report/tier1/(?P<format>JSON/|CSV/|)/?$', rebus_tier1_views.customised),

##### INTERNGI REPORT
    url(r'^report/interngi/(?P<query>[\w-]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/$', views.report_interngi),
    url(r'^report/interngi/$', views.report_interngi),

##### VOMET REPORT
    url(r'^report/vomet/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/$', views.report_vomet),
    url(r'^report/vomet/$', views.report_vomet),

##### Discipline API
    url(r'^disciplines/cloud/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<format>JSON|CSV)/$', views_api.discipline_cloud_view),
    url(r'^discipline/cloud/(?P<discipline>[^/]*?)/(?P<format>JSON|CSV)/$', views_api.discipline_cloud_view),
    url(r'^disciplines/cloud/(?P<format>JSON|CSV)/$', views_api.discipline_cloud_view),
    url(r'^discipline/cloud/(?P<discipline>[^/]*?)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<format>JSON|CSV)/$', views_api.discipline_cloud_view),
    url(r'^disciplines/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<format>JSON|CSV)/$', views_api.discipline_view),
    url(r'^disciplines/(?P<format>JSON|CSV)/$', views_api.discipline_view),
    url(r'^discipline/(?P<discipline>[^/]*?)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<format>JSON|CSV)/$', views_api.discipline_view),
    url(r'^discipline/(?P<discipline>[^/]*?)/(?P<format>JSON|CSV)/$', views_api.discipline_view),

##### Discipline 
    url(r'^disciplines/cloud/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/$', views.discipline_cloud_view),
    url(r'^discipline/cloud/(?P<discipline>[^/]*?)/$', views.discipline_cloud_view),
    url(r'^disciplines/cloud/$', views.discipline_cloud_view),
    url(r'^discipline/cloud/(?P<discipline>[^/]*?)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/$', views.discipline_cloud_view),
    url(r'^disciplines/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/$', views.discipline_view),
    url(r'^disciplines/$', views.discipline_view),
    url(r'^discipline/(?P<discipline>[^/]*?)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/$', views.discipline_view),
    url(r'^discipline/(?P<discipline>[^/]*?)/$', views.discipline_view),

##### TIER1 CLOUD APIS
    url(r'^(?P<wlcg>wlcg/|)?tier1/cloud/node/(?P<node>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.tier1_cloud_node_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/cloud/node/(?P<node>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.tier1_cloud_node_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/cloud/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.tier1_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/cloud/site/(?P<site>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.tier1_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/cloud/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.tier1_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/cloud/(?P<format>JSON|CSV)/$', views_api.tier1_cloud_view),

##### TIER1 CLOUD
    url(r'^(?P<wlcg>wlcg/|)?tier1/cloud/node/(?P<node>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.tier1_cloud_node_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/cloud/node/(?P<node>[\w-]+)/$', views.tier1_cloud_node_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/cloud/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.tier1_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/cloud/site/(?P<site>[\w-]+)/$', views.tier1_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/cloud/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.tier1_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/cloud/$', views.tier1_cloud_view),

##### TIER1 APIS
    url(r'^(?P<wlcg>wlcg/|)?tier1/node/(?P<node>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.tier1_node_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/node/(?P<node>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.tier1_node_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.tier1_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/site/(?P<site>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.tier1_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.tier1_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/(?P<format>JSON|CSV)/$', views_api.tier1_view),

##### TIER1
    url(r'^(?P<wlcg>wlcg/|)?tier1/node/(?P<node>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.tier1_node_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/node/(?P<node>[\w-]+)/$', views.tier1_node_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.tier1_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/site/(?P<site>[\w-]+)/$', views.tier1_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.tier1_view),
    url(r'^(?P<wlcg>wlcg/|)?tier1/$', views.tier1_view),

##### TIER2 CLOUD APIS
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.tier2_cloud_country_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/country/(?P<country>[\w\s-]+)/(?P<format>JSON|CSV)/$', views_api.tier2_cloud_country_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/federation/(?P<federation>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.tier2_cloud_federation_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/federation/(?P<federation>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.tier2_cloud_federation_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.tier2_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/site/(?P<site>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.tier2_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.tier2_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/(?P<format>JSON|CSV)/$', views_api.tier2_cloud_view),

##### TIER2 CLOUD
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.tier2_cloud_country_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/country/(?P<country>[\w\s-]+)/$', views.tier2_cloud_country_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/federation/(?P<federation>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.tier2_cloud_federation_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/federation/(?P<federation>[\w-]+)/$', views.tier2_cloud_federation_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.tier2_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/site/(?P<site>[\w-]+)/$', views.tier2_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.tier2_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/cloud/$', views.tier2_cloud_view),

##### TIER2 APIS
    url(r'^(?P<wlcg>wlcg/|)?tier2/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.tier2_country_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/country/(?P<country>[\w\s-]+)/(?P<format>JSON|CSV)/$', views_api.tier2_country_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/federation/(?P<federation>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.tier2_federation_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/federation/(?P<federation>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.tier2_federation_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.tier2_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/site/(?P<site>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.tier2_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.tier2_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/(?P<format>JSON|CSV)/$', views_api.tier2_view),

##### TIER2
    url(r'^(?P<wlcg>wlcg/|)?tier2/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.tier2_country_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/country/(?P<country>[\w\s-]+)/$', views.tier2_country_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/federation/(?P<federation>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.tier2_federation_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/federation/(?P<federation>[\w-]+)/$', views.tier2_federation_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.tier2_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/site/(?P<site>[\w-]+)/$', views.tier2_site_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.tier2_view),
    url(r'^(?P<wlcg>wlcg/|)?tier2/$', views.tier2_view),

##### EGI API 
    url(r'^egi/ngi/(?P<ngi>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.egi_ngi_view),
    url(r'^egi/ngi/(?P<ngi>[\w-]+)/(?P<format>JSON|CSV|)/$', views_api.egi_ngi_view),
    url(r'^egi/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.egi_country_view),
    url(r'^egi/country/(?P<country>[\w\s-]+)/(?P<format>JSON|CSV)/$', views_api.egi_country_view),
    url(r'^egi/countries/(?P<query>[\w\s]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.egi_countries_view),
    url(r'^egi/countries/(?P<format>JSON|CSV)/$', views_api.egi_countries_view),
    url(r'^egi/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.egi_site_view),
    url(r'^egi/site/(?P<site>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.egi_site_view),
    url(r'^egi/(?P<format>JSON|CSV)/$', views_api.egi_view),
    url(r'^egi/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.egi_view),
    url(r'^egi/(?P<query>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.egi_view),

##### EGI 
    url(r'^egi/ngi/(?P<ngi>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.egi_ngi_view),
    url(r'^egi/ngi/(?P<ngi>[\w-]+)/?$', views.egi_ngi_view),
    url(r'^egi/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.egi_country_view),
    url(r'^egi/country/(?P<country>[\w\s-]+)/?$', views.egi_country_view),
    url(r'^egi/countries/(?P<query>[\w\s]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.egi_countries_view),
    url(r'^egi/countries/?$', views.egi_countries_view),
    url(r'^egi/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.egi_site_view),
    url(r'^egi/site/(?P<site>[\w-]+)/$', views.egi_site_view),
    url(r'^egi/$', views.egi_view),
    url(r'^egi/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.egi_view),
    url(r'^egi/(?P<query>[\w-]+)/$', views.egi_view),

##### Storage API
    url(r'^storage/countries/(?P<query>[\w\s]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.storage_countries_view),
    url(r'^storage/countries/(?P<format>JSON|CSV)/$', views_api.storage_countries_view),
    url(r'^storage/(?P<query>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.storage_view),
    url(r'^storage/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.storage_view),
    url(r'^storage/ngi/(?P<ngi>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.storage_ngi_view),
    url(r'^storage/ngi/(?P<ngi>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.storage_ngi_view),
    url(r'^storage/country/(?P<country>[\w\s-]+)/(?P<format>JSON|CSV)/$', views_api.storage_country_view),
    url(r'^storage/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.storage_country_view),
    url(r'^storage/(?P<format>JSON|CSV)/$', views_api.storage_view),
    url(r'^storage/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.storage_site_view),
    url(r'^storage/site/(?P<site>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.storage_site_view),

##### Storage 
    url(r'^storage/countries/(?P<query>[\w\s]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.storage_countries_view),
    url(r'^storage/countries/$', views.storage_countries_view),
    url(r'^storage/(?P<query>[\w-]+)/$', views.storage_view),
    url(r'^storage/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.storage_view),
    url(r'^storage/ngi/(?P<ngi>[\w-]+)/$', views.storage_ngi_view),
    url(r'^storage/ngi/(?P<ngi>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.storage_ngi_view),
    url(r'^storage/country/(?P<country>[\w\s-]+)/$', views.storage_country_view),
    url(r'^storage/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.storage_country_view),
    url(r'^storage/$', views.storage_view),
    url(r'^storage/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.storage_site_view),
    url(r'^storage/site/(?P<site>[\w-]+)/$', views.storage_site_view),

##### WLCG API
    url(r'^wlcg/country/(?P<country>[\w\s-]+)/(?P<format>JSON|CSV)/$', views_api.wlcg_country_view),
    url(r'^wlcg/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.wlcg_country_view),
    url(r'^wlcg/(?P<format>JSON|CSV)/$', views_api.wlcg_view),
    url(r'^wlcg/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.wlcg_site_view),
    url(r'^wlcg/site/(?P<site>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.wlcg_site_view),

##### WLCG Standard 
    url(r'^wlcg/country/(?P<country>[\w\s-]+)/$', views.wlcg_country_view),
    url(r'^wlcg/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.wlcg_country_view),
    url(r'^wlcg/$', views.wlcg_view),
    url(r'^wlcg/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.wlcg_site_view),
    url(r'^wlcg/site/(?P<site>[\w-]+)/$', views.wlcg_site_view),

##### OSG API
    url(r'^(?P<wlcg>wlcg/|)?osg/cloud/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.osg_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?osg/cloud/(?P<format>JSON|CSV)/$', views_api.osg_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?osg/cloud/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.osg_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?osg/cloud/site/(?P<site>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.osg_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?osg/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.osg_view),
    url(r'^(?P<wlcg>wlcg/|)?osg/(?P<format>JSON|CSV)/$', views_api.osg_view),
    url(r'^(?P<wlcg>wlcg/|)?osg/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.osg_site_view),
    url(r'^(?P<wlcg>wlcg/|)?osg/site/(?P<site>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.osg_site_view),

##### OSG
    url(r'^(?P<wlcg>wlcg/|)?osg/cloud/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.osg_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?osg/cloud/$', views.osg_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?osg/cloud/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.osg_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?osg/cloud/site/(?P<site>[\w-]+)/$', views.osg_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?osg/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.osg_view),
    url(r'^(?P<wlcg>wlcg/|)?osg/$', views.osg_view),
    url(r'^(?P<wlcg>wlcg/|)?osg/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.osg_site_view),
    url(r'^(?P<wlcg>wlcg/|)?osg/site/(?P<site>[\w-]+)/$', views.osg_site_view),

##### SITE ADMIN API
    url(r'^(?P<wlcg>wlcg/|)?site_admin/cloud/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.site_admin_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?site_admin/cloud/(?P<format>JSON|CSV)/$', views_api.site_admin_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?site_admin/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.site_admin_view),
    url(r'^(?P<wlcg>wlcg/|)?site_admin/(?P<format>JSON|CSV)/$', views_api.site_admin_view),

##### SITE ADMIN 
    url(r'^(?P<wlcg>wlcg/|)?site_admin/cloud/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.site_admin_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?site_admin/cloud/$', views.site_admin_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?site_admin/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.site_admin_view),
    url(r'^(?P<wlcg>wlcg/|)?site_admin/$', views.site_admin_view),

##### VO ADMIN CLOUD API
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/site/(?P<site>[\w-]+)/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<format>JSON|CSV)/$', views_api.vo_admin_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/site/(?P<site>[\w-]+)/(?P<vo>[\W\w\s]+)/(?P<format>JSON|CSV)/$', views_api.vo_admin_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/ngi/(?P<ngi>[\w-]+)/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<format>JSON|CSV)/$', views_api.vo_admin_cloud_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/ngi/(?P<ngi>[\w-]+)/(?P<vo>[\W\w\s]+)/(?P<format>JSON|CSV)/$', views_api.vo_admin_cloud_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/country/(?P<country>[\w\s-]+)/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<format>JSON|CSV)/$', views_api.vo_admin_cloud_country_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/country/(?P<country>[\w\s-]+)/(?P<vo>[\W\w\s]+)/(?P<format>JSON|CSV)/$', views_api.vo_admin_cloud_country_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<format>JSON|CSV)/$', views_api.vo_admin_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/(?P<format>JSON|CSV)/$', views_api.vo_admin_cloud_view),

##### VO ADMIN CLOUD 
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/site/(?P<site>[\w-]+)/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/$', views.vo_admin_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/site/(?P<site>[\w-]+)/(?P<vo>[\W\w\s]+)/$', views.vo_admin_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/ngi/(?P<ngi>[\w-]+)/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/$', views.vo_admin_cloud_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/ngi/(?P<ngi>[\w-]+)/(?P<vo>[\W\w\s]+)/$', views.vo_admin_cloud_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/country/(?P<country>[\w\s-]+)/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/$', views.vo_admin_cloud_country_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/country/(?P<country>[\w\s-]+)/(?P<vo>[\W\w\s]+)/$', views.vo_admin_cloud_country_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/$', views.vo_admin_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/cloud/$', views.vo_admin_cloud_view),

##### VO ADMIN API
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/site/(?P<site>[\w-]+)/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.vo_admin_site_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/site/(?P<site>[\w-]+)/(?P<vo>[\W\w\s]+)/(?P<format>JSON|CSV)/$', views_api.vo_admin_site_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/ngi/(?P<ngi>[\w-]+)/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.vo_admin_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/ngi/(?P<ngi>[\w-]+)/(?P<vo>[\W\w\s]+)/(?P<format>JSON|CSV)/$', views_api.vo_admin_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/country/(?P<country>[\w\s-]+)/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.vo_admin_country_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/country/(?P<country>[\w\s-]+)/(?P<vo>[\W\w\s]+)/(?P<format>JSON|CSV)/$', views_api.vo_admin_country_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<format>JSON|CSV)/$', views_api.vo_admin_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/(?P<format>JSON|CSV)/$', views_api.vo_admin_view),

##### VO ADMIN 
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/site/(?P<site>[\w-]+)/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.vo_admin_site_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/site/(?P<site>[\w-]+)/(?P<vo>[\W\w\s]+)/$', views.vo_admin_site_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/ngi/(?P<ngi>[\w-]+)/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.vo_admin_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/ngi/(?P<ngi>[\w-]+)/(?P<vo>[\W\w\s]+)/$', views.vo_admin_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/country/(?P<country>[\w\s-]+)/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.vo_admin_country_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/country/(?P<country>[\w\s-]+)/(?P<vo>[\W\w\s]+)/$', views.vo_admin_country_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/(?P<vo>[\W\w\s]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/$', views.vo_admin_view),
    url(r'^(?P<wlcg>wlcg/|)?vo_admin/$', views.vo_admin_view),

##### USER VIEW CLOUD API
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.user_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/site/(?P<site>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.user_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/ngi/(?P<ngi>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.user_cloud_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/ngi/(?P<ngi>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.user_cloud_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.user_cloud_country_view),
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/country/(?P<country>[\w\s-]+)/(?P<format>JSON|CSV)/$', views_api.user_cloud_country_view),
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.user_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/(?P<format>JSON|CSV)/$', views_api.user_cloud_view),

##### USER VIEW CLOUD
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.user_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/site/(?P<site>[\w-]+)/$', views.user_cloud_site_view),
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/ngi/(?P<ngi>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.user_cloud_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/ngi/(?P<ngi>[\w-]+)/$', views.user_cloud_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.user_cloud_country_view),
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/country/(?P<country>[\w\s-]+)/$', views.user_cloud_country_view),
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.user_cloud_view),
    url(r'^(?P<wlcg>wlcg/|)?user/cloud/$', views.user_cloud_view),

##### USER VIEW API
    url(r'^(?P<wlcg>wlcg/|)?user/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.user_site_view),
    url(r'^(?P<wlcg>wlcg/|)?user/site/(?P<site>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.user_site_view),
    url(r'^(?P<wlcg>wlcg/|)?user/ngi/(?P<ngi>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.user_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?user/ngi/(?P<ngi>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.user_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?user/country/(?P<country>[\w\s-]+)/(?P<format>JSON|CSV)/$', views_api.user_country_view),
    url(r'^(?P<wlcg>wlcg/|)?user/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.user_country_view),
    url(r'^(?P<wlcg>wlcg/|)?user/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.user),
    url(r'^(?P<wlcg>wlcg/|)?user/(?P<format>JSON|CSV)/$', views_api.user),

##### USER VIEW
    url(r'^(?P<wlcg>wlcg/|)?user/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.user_site_view),
    url(r'^(?P<wlcg>wlcg/|)?user/site/(?P<site>[\w-]+)/$', views.user_site_view),
    url(r'^(?P<wlcg>wlcg/|)?user/ngi/(?P<ngi>[\w-]+)/$', views.user_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?user/ngi/(?P<ngi>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.user_ngi_view),
    url(r'^(?P<wlcg>wlcg/|)?user/country/(?P<country>[\w\s-]+)/$', views.user_country_view),
    url(r'^(?P<wlcg>wlcg/|)?user/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.user_country_view),
    url(r'^(?P<wlcg>wlcg/|)?user/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.user),
    url(r'^(?P<wlcg>wlcg/|)?user/$', views.user),

##### CLOUD API
    url(r'^cloud/countries/(?P<query>[\w\s]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.cloud_countries_view),
    url(r'^cloud/countries/(?P<format>JSON|CSV)/$', views_api.cloud_countries_view),
    url(r'^cloud/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.cloud_view),
    url(r'^cloud/(?P<format>JSON|CSV)/$', views_api.cloud_view),
    url(r'^cloud/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.cloud_site_view),
    url(r'^cloud/site/(?P<site>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.cloud_site_view),
    url(r'^cloud/ngi/(?P<ngi>[\w-]+)/(?P<format>JSON|CSV)/$', views_api.cloud_ngi_view),
    url(r'^cloud/ngi/(?P<ngi>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.cloud_ngi_view),
    url(r'^cloud/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.cloud_country_view),
    url(r'^cloud/country/(?P<country>[\w\s-]+)/(?P<format>JSON|CSV)/$', views_api.cloud_country_view),

##### CLOUD
    url(r'^cloud/countries/(?P<query>[\w\s]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.cloud_countries_view),
    url(r'^cloud/countries/$', views.cloud_countries_view),
    url(r'^cloud/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.cloud_view),
    url(r'^cloud/$', views.cloud_view),
    url(r'^cloud/site/(?P<site>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.cloud_site_view),
    url(r'^cloud/site/(?P<site>[\w-]+)/$', views.cloud_site_view),
    url(r'^cloud/ngi/(?P<ngi>[\w-]+)/$', views.cloud_ngi_view),
    url(r'^cloud/ngi/(?P<ngi>[\w-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.cloud_ngi_view),
    url(r'^cloud/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.cloud_country_view),
    url(r'^cloud/country/(?P<country>[\w\s-]+)/$', views.cloud_country_view),

#### WLCG ALL COUNTRIES API
    url(r'^wlcg/country/(?P<country>[\w\s-]+)/(?P<format>JSON|CSV)/$', views_api.wlcg_country_view),
    url(r'^wlcg/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.wlcg_country_view),
    url(r'^wlcg/countries/(?P<query>[\w\s]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/(?P<format>JSON|CSV)/$', views_api.wlcg_countries_view),
    url(r'^wlcg/countries/(?P<format>JSON|CSV)/$', views_api.wlcg_countries_view),
    url(r'^wlcg/(?P<format>JSON|CSV)/$', views_api.wlcg_view),

#### WLCG ALL COUNTRIES
    url(r'^wlcg/country/(?P<country>[\w\s-]+)/$', views.wlcg_country_view),
    url(r'^wlcg/country/(?P<country>[\w\s-]+)/(?P<query>[\w-]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.wlcg_country_view),
    url(r'^wlcg/countries/(?P<query>[\w\s]+)/(?P<yRange>[\w\s]+)/(?P<xRange>[\w\s]+)/(?P<sYear>\d\d\d\d)/(?P<sMonth>\d{1,2})/(?P<eYear>\d\d\d\d)/(?P<eMonth>\d{1,2})/(?P<VOGroup>[\w\S]+)/(?P<localJobGroup>[\w]+)/$', views.wlcg_countries_view),
    url(r'^wlcg/countries/$', views.wlcg_countries_view),
    url(r'^wlcg/$', views.wlcg_view),
]
