from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def main_view(request):
  return render_to_response("main_page.html", {}, 
         context_instance=RequestContext(request))

def report_interngi(request, query='njobs', sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("interngi_report.html", {'url':'report/interngi/', 'query': query, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def report_rc(request, sMonth = None, eMonth = None, sYear = None, eYear = None, report = 'top10', infra = 'htc'):
  return render_to_response("report_rc.html", {'url':'report/resource_centers/', 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'report': report, 'infra': infra}, 
         context_instance=RequestContext(request))

def report_dis(request, sMonth = None, eMonth = None, sYear = None, eYear = None, infra = 'htc', disciplines = 'Natural Sciences'):
  return render_to_response("report_dis.html", {'url':'report/disciplines/', 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'infra': infra, 'disciplines': disciplines}, 
         context_instance=RequestContext(request))

def report_vomet(request, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("egi_report_vomet.html", {'url':'report/vomet/', 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def wlcg_report_tier2(request, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("wlcg_report_tier2.html", {'url':'wlcg/report/tier2/', 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'tier2': 'True'}, 
         context_instance=RequestContext(request))

def wlcg_report_countries(request, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("wlcg_report_countries.html", {'url':'wlcg/report/countries/', 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def tier1_cloud_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("tier1_cloud.html", {'url':'tier1/cloud/', 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier1_cloud_node_view(request, query = None, node = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("tier1_cloud.html", {'url':'tier1/cloud/node/'+node+'/', 'node': node, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier1_cloud_site_view(request, query = None, site = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("tier1_cloud.html", {'url':'tier1/cloud/site/'+site+'/', 'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_cloud_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("tier2_cloud.html", {'url':'tier2/cloud/', 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_cloud_country_view(request, query = None, country = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("tier2_cloud.html", {'url':'tier2/cloud/country/'+country+'/', 'country': country, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_cloud_federation_view(request, query = None, federation = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("tier2_cloud.html", {'url':'tier2/cloud/federation/'+federation+'/', 'federation': federation, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_cloud_site_view(request, query = None, site = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("tier2_cloud.html", {'url':'tier2/cloud/site/'+site+'/', 'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier1_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("tier1.html", {'url':'tier1/', 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier1_node_view(request, query = None, node = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("tier1.html", {'url':'tier1/node/'+node+'/', 'node': node, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier1_site_view(request, query = None, site = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("tier1.html", {'url':'tier1/site/'+site+'/', 'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("tier2.html", {'url':'tier2/', 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_country_view(request, query = None, country = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("tier2.html", {'url':'tier2/country/'+country+'/', 'country': country, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_federation_view(request, query = None, federation = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("tier2.html", {'url':'tier2/federation/'+federation+'/', 'federation': federation, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def tier2_site_view(request, query = None, site = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("tier2.html", {'url':'tier2/site/'+site+'/', 'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def osg_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("osg.html", {'url':'osg/', 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def osg_site_view(request, site, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("osg.html", {'url':'osg/site/'+site+'/', 'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup},         context_instance=RequestContext(request))

def osg_cloud_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("osg_cloud.html", {'url':'osg/cloud/', 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def osg_cloud_site_view(request, site, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("osg_cloud.html", {'url':'osg/cloud/site/'+site+'/', 'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup},         context_instance=RequestContext(request))

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

def wlcg_countries_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("egi.html", {'url':'wlcg/countries/','query': query, 'ovw_country': 'True', 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup, 'allcountry_ovw': True}, 
         context_instance=RequestContext(request))

def wlcg_country_view(request, country, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlyinfrajobs"):
  return render_to_response("egi.html", {'url':'wlcg/country/'+country+'/', 'country': country, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup, 'allcountry': True}, 
         context_instance=RequestContext(request))

def site_admin_view(request, site = '', query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("userdn.html", {'site_admin': True, 'site': site, 'role':'site_admin', 'url':'site_admin/','query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def site_admin_cloud_view(request, site = '', query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("userdn_cloud.html", {'site_admin': True, 'site': site, 'role':'site_admin', 'url':'site_admin/cloud/','query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def vo_admin_view(request, vo = '', query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("userdn.html", {'vo_admin': True, 'vo': vo, 'role':'vo_admin', 'url':'vo_admin/','query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def vo_admin_site_view(request, site, vo = "", query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("userdn.html", {'vo_admin': True, 'site': site, 'vo': vo, 'role':'vo_admin', 'url':'vo_admin/site/'+site+'/', 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear},         context_instance=RequestContext(request))

def vo_admin_ngi_view(request, ngi, vo = '', query = None, xRange = None, yRange = None, option="roc", sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("userdn.html", {'vo_admin': True, 'ngi': ngi, 'vo': vo, 'role':'vo_admin', 'url':'vo_admin/ngi/'+ngi+'/', 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def vo_admin_country_view(request, country, vo = '', query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("userdn.html", {'vo_admin': True, 'country': country, 'vo': vo, 'role':'vo_admin', 'url':'vo_admin/country/'+country+'/', 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def vo_admin_cloud_view(request, vo = '', query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("userdn_cloud.html", {'vo_admin': True, 'vo': vo, 'role':'vo_admin', 'url':'vo_admin/cloud/','query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def vo_admin_cloud_site_view(request, vo = '', site = None, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("userdn_cloud.html", {'vo_admin': True, 'site': site, 'vo': vo, 'role':'vo_admin', 'url':'vo_admin/cloud/site/'+site+'/','site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear},
         context_instance=RequestContext(request))

def vo_admin_cloud_ngi_view(request, ngi = None, vo = '', query = None, xRange = None, yRange = None, option="roc", sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("userdn_cloud.html", {'vo_admin': True, 'ngi': ngi, 'vo': vo, 'role':'vo_admin', 'url':'vo_admin/cloud/ngi/'+ngi+'/', 'ngi': ngi, 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def vo_admin_cloud_country_view(request, country = None, vo = '', query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("userdn_cloud.html", {'vo_admin': True, 'country': country, 'vo': vo, 'role':'vo_admin', 'url':'vo_admin/cloud/country/'+country+'/', 'country': country, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def user_view_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("userdn.html", {'user_view': True, 'role':'user_view', 'url':'user_view/','query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def user_view_site_view(request, site, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("userdn.html", {'user_view': True, 'site': site, 'role':'user_view', 'url':'user_view/site/'+site+'/', 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup},         context_instance=RequestContext(request))

def user_view_ngi_view(request, ngi, query = None, xRange = None, yRange = None, option="roc", sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("userdn.html", {'user_view': True, 'ngi': ngi, 'role':'user_view', 'url':'user_view/ngi/'+ngi+'/', 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def user_view_country_view(request, country, vo = '', query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("userdn.html", {'user_view': True, 'country': country, 'vo': '', 'role':'user_view', 'url':'user_view/country/'+country+'/', 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def user_view_cloud_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("userdn_cloud.html", {'user_view': True, 'vo': '', 'role':'user_view', 'url':'user_view/cloud/','query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def user_view_cloud_site_view(request, site = None, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("userdn_cloud.html", {'user_view': True, 'site': site, 'vo': '', 'role':'user_view', 'url':'user_view/cloud/site/'+site+'/','site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup},
         context_instance=RequestContext(request))

def user_view_cloud_ngi_view(request, ngi = None, query = None, xRange = None, yRange = None, option="roc", sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("userdn_cloud.html", {'user_view': True, 'ngi': ngi, 'vo': '', 'role':'user_view', 'url':'user_view/cloud/ngi/'+ngi+'/', 'ngi': ngi, 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def user_view_cloud_country_view(request, country = None, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
  return render_to_response("userdn_cloud.html", {'user_view': True, 'country': country, 'vo': '', 'role':'user_view', 'url':'user_view/cloud/country/'+country+'/', 'country': country, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
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

def cloud_countries_view(request, query = 'vm_num', xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="egi", localJobGroup="onlyinfrajobs"):
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
