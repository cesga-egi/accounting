from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def main_view(request):
  return render_to_response("main_page.html", {}, 
         context_instance=RequestContext(request))

def egi_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlygridjobs"):
  return render_to_response("egi.html", {'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def egi_site_view(request, site, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlygridjobs"):
  return render_to_response("egi.html", {'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup},         context_instance=RequestContext(request))

def egi_ngi_view(request, ngi, query = None, xRange = None, yRange = None, option="roc", sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("egi.html", {'ngi': ngi, 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def egi_country_view(request, country, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("egi.html", {'country': country, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def user_dn_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlygridjobs"):
  return render_to_response("userdn.html", {'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

def user_dn_site_view(request, site, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlygridjobs"):
  return render_to_response("userdn.html", {'site': site, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup},         context_instance=RequestContext(request))

def user_dn_ngi_view(request, ngi, query = None, xRange = None, yRange = None, option="roc", sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("userdn.html", {'ngi': ngi, 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def user_dn_country_view(request, country, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("userdn.html", {'country': country, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))


def cloud_view(request, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("cloud.html", {'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def cloud_site_view(request, site, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("cloud.html", {'site': site, 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def cloud_ngi_view(request, ngi, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("cloud.html", {'ngi': ngi, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def cloud_country_view(request, country, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None):
  return render_to_response("cloud.html", {'country': country, 'query': query,'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear}, 
         context_instance=RequestContext(request))

def discipline_view(request, discipline= None, query = None, xRange = None, yRange = None, sMonth = None, eMonth = None, sYear = None, eYear = None, VOGroup="lhc", localJobGroup="onlygridjobs"):
  return render_to_response("vodis.html", {'discipline': discipline, 'query': query, 'xRange': xRange, 'yRange': yRange, 'sMonth': sMonth, 'eMonth': eMonth, 'sYear': sYear, 'eYear': eYear, 'VOGroup': VOGroup, 'localJobGroup': localJobGroup}, 
         context_instance=RequestContext(request))

