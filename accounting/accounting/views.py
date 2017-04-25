from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def main_view(request):
  return render_to_response("main_page.html", {}, 
         context_instance=RequestContext(request))

def wlcg_view(request):
  return redirect('/wlcg/countries/')

def report_interngi(request, query='njobs', sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("interngi_report.html", {'url':'report/interngi/', 'query': query, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def report_rc(request, sMonth = None, eMonth = None, sYear = None, eYear = None, report = 'top10', infra = 'htc'):
  return render_to_response("report_rc.html", {'url':'report/resource_centres/', 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'report': report, 'infra': infra}, 
         context_instance=RequestContext(request))

def report_dis(request, sMonth = None, eMonth = None, sYear = None, eYear = None, infra = 'htc', disciplines = 'Natural Sciences'):
  return render_to_response("report_dis.html", {'url':'report/disciplines/', 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'infra': infra, 'disciplines': disciplines}, 
         context_instance=RequestContext(request))

def report_vomet(request, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("egi_report_vomet.html", {'url':'report/vomet/', 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def wlcg_report_tier2(request, sMonth = None, eMonth = None, sYear = None, eYear = None, days = None):
  return render_to_response("wlcg_report_tier2.html", {'day_used': True, 'days': days, 'url':'wlcg/report/tier2/', 'wlcg': 'wlcg/', 'wlcg_page': True, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'tier2': 'True'}, 
         context_instance=RequestContext(request))

def wlcg_report_countries(request, sMonth = None, eMonth = None, sYear = None, eYear = None, days = None):
  return render_to_response("wlcg_report_countries.html", {'day_used': True, 'days': days, 'url':'wlcg/report/countries/', 'wlcg': 'wlcg/', 'wlcg_page': True, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def tier1_cloud_view(request, wlcg = False, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'tier1/cloud/'
  return render_to_response("tier1_cloud.html", {'url': url, 'query': query, 'wlcg': wlcg, 'wlcg_page': True, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier1_cloud_node_view(request, wlcg = False, query = None, node = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'tier1/cloud/node/'+node+'/'
  return render_to_response("tier1_cloud.html", {'url': url, 'wlcg': wlcg, 'wlcg_page': True, 'node': node, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier1_cloud_site_view(request, wlcg = False, query = None, site = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'tier1/cloud/site/'+site+'/'
  return render_to_response("tier1_cloud.html", {'url': url, 'wlcg': wlcg, 'wlcg_page': True, 'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_cloud_view(request, wlcg = False, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'tier2/cloud/'
  return render_to_response("tier2_cloud.html", {'url': url, 'query': query, 'wlcg': wlcg, 'wlcg_page': True, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_cloud_country_view(request, wlcg = False, query = None, country = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'tier2/cloud/country/'+country+'/'
  return render_to_response("tier2_cloud.html", {'url': url, 'wlcg': wlcg, 'wlcg_page': True, 'country': country, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_cloud_federation_view(request, wlcg = False, query = None, federation = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'tier2/cloud/federation/'+federation+'/'
  return render_to_response("tier2_cloud.html", {'url': url, 'wlcg': wlcg, 'wlcg_page': True, 'federation': federation, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_cloud_site_view(request, wlcg = False, query = None, site = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'tier2/cloud/site/'+site+'/'
  return render_to_response("tier2_cloud.html", {'url': url, 'site': site, 'wlcg': wlcg, 'wlcg_page': True, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier1_view(request, wlcg = False, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'tier1/'
  return render_to_response("tier1.html", {'url': url, 'query': query, 'xRange': xRange, 'wlcg': wlcg, 'wlcg_page': True, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier1_node_view(request, wlcg = False, query = None, node = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'tier1/node/'+node+'/'
  return render_to_response("tier1.html", {'url': url, 'node': node, 'wlcg': wlcg, 'wlcg_page': True, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier1_site_view(request, wlcg = False, query = None, site = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'tier1/site/'+site+'/'
  return render_to_response("tier1.html", {'url': url, 'wlcg': wlcg, 'wlcg_page': True, 'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_view(request, wlcg = False, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'tier2/'
  return render_to_response("tier2.html", {'url': url, 'query': query, 'wlcg': wlcg, 'wlcg_page': True, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_country_view(request, wlcg = False, query = None, country = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'tier2/country/'+country+'/'
  return render_to_response("tier2.html", {'url': url, 'wlcg': wlcg, 'wlcg_page': True, 'country': country, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_federation_view(request, wlcg = False, query = None, federation = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'tier2/federation/'+federation+'/'
  return render_to_response("tier2.html", {'url': url, 'wlcg': wlcg, 'wlcg_page': True, 'federation': federation, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_site_view(request, wlcg = False, query = None, site = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'tier2/site/'+site+'/'
  return render_to_response("tier2.html", {'url': url, 'wlcg': wlcg, 'wlcg_page': True, 'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def osg_view(request, wlcg = False, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'osg/'
  return render_to_response("osg.html", {'url': url, 'query': query, 'wlcg': wlcg, 'wlcg_page': True, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def osg_site_view(request, site, wlcg = False, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'osg/site/'+site+'/'
  return render_to_response("osg.html", {'url': url, 'wlcg': wlcg, 'wlcg_page': True, 'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup},         context_instance=RequestContext(request))

def osg_cloud_view(request, wlcg = False, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'osg/cloud/'
  return render_to_response("osg_cloud.html", {'url': url, 'wlcg': wlcg, 'wlcg_page': True, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def osg_cloud_site_view(request, site, wlcg = False, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  url = ('wlcg/' if wlcg else '') + 'osg/cloud/site/'+site+'/'
  return render_to_response("osg_cloud.html", {'url': url, 'wlcg': wlcg, 'wlcg_page': True, 'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup},         context_instance=RequestContext(request))

def egi_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("egi.html", {'url':'egi/', 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def egi_site_view(request, site, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("egi.html", {'url':'egi/site/'+site+'/', 'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup},         context_instance=RequestContext(request))

def egi_ngi_view(request, ngi, query = None, xRange = None, yRange = None, option="roc", sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("egi.html", {'url':'egi/ngi/'+ngi+'/', 'ngi': ngi, 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def egi_country_view(request, country, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("egi.html", {'url':'egi/country/'+country+'/', 'country': country, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def egi_countries_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("egi.html", {'url':'egi/countries/','query': query, 'ovw_country': 'True', 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def storage_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("storage.html", {'url':'storage/', 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def storage_site_view(request, site, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("storage.html", {'url':'storage/site/'+site+'/', 'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup},         context_instance=RequestContext(request))

def storage_ngi_view(request, ngi, query = None, xRange = None, yRange = None, option="roc", sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("storage.html", {'url':'storage/ngi/'+ngi+'/', 'ngi': ngi, 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def storage_country_view(request, country, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("storage.html", {'url':'storage/country/'+country+'/', 'country': country, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def storage_countries_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("storage.html", {'url':'storage/countries/','query': query, 'ovw_country': 'True', 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))
def wlcg_countries_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("wlcg.html", {'url':'wlcg/countries/','query': query, 'wlcg': 'wlcg/', 'wlcg_page': True, 'ovw_country': 'True', 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup, 'allcountry_ovw': True}, 
         context_instance=RequestContext(request))

def wlcg_country_view(request, country, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("wlcg.html", {'url':'wlcg/country/'+country+'/', 'wlcg_page': True, 'wlcg': 'wlcg/', 'country': country, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup, 'allcountry': True}, 
         context_instance=RequestContext(request))

def wlcg_site_view(request, site, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("wlcg.html", {'url':'wlcg/site/'+site+'/', 'wlcg': 'wlcg/', 'wlcg_page': True, 'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup},         context_instance=RequestContext(request))

def site_admin_view(request, wlcg = False, site = '', query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'site_admin/'
  return render_to_response("userdn.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'site_admin': True, 'site': site, 'role':'site_admin', 'url': url,'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def site_admin_cloud_view(request, wlcg = False, site = '', query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'site_admin/cloud/'
  return render_to_response("userdn_cloud.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'site_admin': True, 'site': site, 'role':'site_admin', 'url':url,'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def vo_admin_view(request, wlcg = False, vo = '', query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'vo_admin/'
  return render_to_response("userdn.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'vo_admin': True, 'vo': vo, 'role':'vo_admin', 'url':url,'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def vo_admin_site_view(request, site, wlcg = False, vo = "", query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'vo_admin/site/'+site+'/'
  return render_to_response("userdn.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'vo_admin': True, 'site': site, 'vo': vo, 'role':'vo_admin', 'url':url, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear},         context_instance=RequestContext(request))

def vo_admin_ngi_view(request, ngi, wlcg = False, vo = '', query = None, xRange = None, yRange = None, option="roc", sMonth = None, eMonth = None, sYear = None, eYear = None):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'vo_admin/ngi/'+ngi+'/'
  return render_to_response("userdn.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'vo_admin': True, 'ngi': ngi, 'vo': vo, 'role':'vo_admin', 'url': url, 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def vo_admin_country_view(request, country, wlcg = False, vo = '', query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'vo_admin/country/'+country+'/'
  return render_to_response("userdn.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'vo_admin': True, 'country': country, 'vo': vo, 'role':'vo_admin', 'url': url, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def vo_admin_cloud_view(request, wlcg = False, vo = '', query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'vo_admin/cloud/'
  return render_to_response("userdn_cloud.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'vo_admin': True, 'vo': vo, 'role':'vo_admin', 'url': url,'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def vo_admin_cloud_site_view(request, wlcg = False, vo = '', site = None, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'vo_admin/cloud/site/'+site+'/'
  return render_to_response("userdn_cloud.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'vo_admin': True, 'site': site, 'vo': vo, 'role':'vo_admin', 'url':url,'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear},
         context_instance=RequestContext(request))

def vo_admin_cloud_ngi_view(request, wlcg = False, ngi = None, vo = '', query = None, xRange = None, yRange = None, option="roc", sMonth = None, eMonth = None, sYear = None, eYear = None):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'vo_admin/cloud/ngi/'+ngi+'/'
  return render_to_response("userdn_cloud.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'vo_admin': True, 'ngi': ngi, 'vo': vo, 'role':'vo_admin', 'url':url, 'ngi': ngi, 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def vo_admin_cloud_country_view(request, wlcg = False, country = None, vo = '', query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'vo_admin/cloud/country/'+country+'/'
  return render_to_response("userdn_cloud.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'vo_admin': True, 'country': country, 'vo': vo, 'role':'vo_admin', 'url':url, 'country': country, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def user(request, wlcg = False, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'user/'
  return render_to_response("userdn.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'user': True, 'role':'user', 'url':url,'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup, 'optval': ''}, 
         context_instance=RequestContext(request))

def user_site_view(request, site, wlcg = False, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'user/site/'+site+'/'
  return render_to_response("userdn.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'user': True, 'site': site, 'role':'user', 'url':url, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup, 'optval': site},         context_instance=RequestContext(request))

def user_ngi_view(request, ngi, wlcg = False, query = None, xRange = None, yRange = None, option="roc", sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'user/ngi/'+ngi+'/'
  return render_to_response("userdn.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'user': True, 'ngi': ngi, 'role':'user', 'url':url, 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup, 'optval': ngi}, 
         context_instance=RequestContext(request))

def user_country_view(request, country, wlcg = False, vo = '', query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'user/country/'+country+'/'
  return render_to_response("userdn.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'user': True, 'country': country, 'vo': '', 'role':'user', 'url':url, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup, 'optval': country}, 
         context_instance=RequestContext(request))

def user_cloud_view(request, wlcg = False, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'user/cloud/'
  return render_to_response("userdn_cloud.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'user': True, 'vo': '', 'role':'user', 'url':url,'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup, 'optval':''}, 
         context_instance=RequestContext(request))

def user_cloud_site_view(request, wlcg = False, site = None, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'user/cloud/site/'+site+'/'
  return render_to_response("userdn_cloud.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'user': True, 'site': site, 'vo': '', 'role':'user', 'url':url,'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup, 'optval':site},
         context_instance=RequestContext(request))

def user_cloud_ngi_view(request, wlcg = False, ngi = None, query = None, xRange = None, yRange = None, option="roc", sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'user/cloud/ngi/'+ngi+'/'
  return render_to_response("userdn_cloud.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'user': True, 'ngi': ngi, 'vo': '', 'role':'user', 'url':url, 'ngi': ngi, 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup, 'optval': ngi}, 
         context_instance=RequestContext(request))

def user_cloud_country_view(request, wlcg = False, country = None, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  wlcg_page = True if wlcg.find('wlcg') != -1 else False;
  url = ('wlcg/' if wlcg else '') + 'user/cloud/country/'+country+'/'
  return render_to_response("userdn_cloud.html", {'wlcg_page': wlcg_page, 'wlcg': wlcg, 'user': True, 'country': country, 'vo': '', 'role':'user', 'url':url, 'country': country, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup, 'optval': country}, 
         context_instance=RequestContext(request))

def cloud_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("cloud.html", {'url':'cloud/', 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def cloud_site_view(request, site, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("cloud.html", {'url':'cloud/site/'+site+'/', 'site': site, 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def cloud_ngi_view(request, ngi, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("cloud.html", {'url':'cloud/ngi/'+ngi+'/', 'ngi': ngi, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def cloud_country_view(request, country, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("cloud.html", {'url':'cloud/country/'+country+'/', 'country': country, 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def cloud_countries_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("cloud.html", {'url':'cloud/countries/', 'ovw_country': 'True', 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def discipline_view(request, discipline= None, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  if (discipline):
     url = 'discipline/'+discipline+'/' 
  else:
     url = 'disciplines/' 
  return render_to_response("vodis.html", {'url':url, 'discipline': discipline, 'cloud': False, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def discipline_cloud_view(request, discipline= None, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  if (discipline):
     url = 'discipline/cloud/'+discipline+'/' 
  else:
     url = 'disciplines/cloud/' 
  return render_to_response("vodis_cloud.html", {'url':url, 'cloud': True, 'discipline': discipline, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))
