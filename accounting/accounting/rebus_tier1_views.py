from __future__ import division
from django.shortcuts import render_to_response
from django.http import HttpResponse  # , HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext

import json

from acc_report_tools.retrieveData import getSourceData
from acc_report_tools.createPages import createPages, calculateMonthNames

import StringIO

from django.views.decorators.cache import cache_page

VO_NAMES = ['ALICE', 'ATLAS', 'CMS', 'LHCb']
vos_lower = ['alice', 'atlas', 'cms', 'lhcb']



YEAR = 2014
CURRENT_MONTH = 4
MONTH_NAME = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'Novmeber', 'December']
FEDERATIONS = ["CA-TRIUMF","CH-CERN","DE-KIT","ES-PIC","FR-CCIN2P3","IT-INFN-CNAF","KR-KISTI-GSDC","NDGF","NL-T1","NRC-KI-T1","RU-JINR-T1","TW-ASGC","UK-T1-RAL","US-FNAL-CMS","US-T1-BNL"]
import sys

def get_menu_data(type):
    title = {}
    breadcrumbs = []
    menus = get_menu()
    for menu in menus:
        for sub in menu['sub_menu']:
            if sub['id'] == "pledge_%s" % type:
                title['app_title'] = menu['title']
                title['app_id'] = menu['id']
                title['view_title'] = sub['title']
                title['view_id'] = sub['id']
                breadcrumbs.append({'title': menu['title'],
                                    'url':   menu['url'], })

                breadcrumbs.append({'title': sub['title'],
                                    'url':   sub['url'], })
    return (title, breadcrumbs)

def get_menu():
    menu = [{'title':    'Accounting',
              'id':       'acc_report',
              'url':      '',
              'sub_menu': [{'title': 'View previous reports',
                            'id':    'browse_report',
                            'url':   '/wlcg/report/tier1/browse'},
                           {'title': 'WLCG Tier1 report',
                            'id':    'customised_report',
                            'url':   '/wlcg/report/tier1/customised_report/'},
                          ]
             }]

    return menu

def get_menu_style():
    menu_style = """
    body.pledge_resources    #topmenu li.pledge_resources,
    body.pledge_requirements #topmenu li.pledge_requirements,
    body.pledge_summary      #topmenu li.pledge_summary,
    body.pledge_validation   #topmenu li.pledge_validation,
    body.pledge_resources    #topmenu #pledge_resources a,
    body.pledge_requirements #topmenu #pledge_requirements a,
    body.pledge_summary      #topmenu #pledge_summary a,
    body.pledge_validation   #topmenu #pledge_validation a {
        color:#0C6DFF !important;
        font-weight: bold;
    }

    """

    return menu_style
def fetch_resources(uri, rel):
    """
    Callback to allow pisa/reportlab to retrieve Images,Stylesheets, etc.
    `uri` is the href attribute from the html link element.
    `rel` gives a relative path, but it's not used here.

    """
    path = '/usr/share/django/' + uri
    return path


def calculateTotals(my_data):

    # Adding up the cpu grid and cpu nongrid
    for at in ('cpu_usage', 'wall_time',):
        for exp in VO_NAMES:
            attribute = "%s_%s" % (exp, at)
            my_data[attribute] = {}
            for site in my_data['grid_%s' % attribute].keys():
                my_data[attribute][site] = []
                a = 'grid_%s' % attribute
                for i in range(0, len(my_data[a][site])):
                    my_data[attribute][site].append(my_data[a][site][i] + my_data['non_' + a][site][i])

    # Now, adding the four experiments
    for at in ('cpu_usage', 'wall_time', 'disk_allocated', 'disk_usage', 'tape_used'):
        for prefix in ('', 'non_grid_', 'grid_'):
            attribute = prefix + at
            my_data[attribute] = {}
            for exp in VO_NAMES:
                a = prefix + exp + '_' + at
                # For hte tape used, the name of the experiment is at the end...
                if at == 'tape_used':
                    a = at + '_' + exp
                if not my_data.has_key(a):
                    continue
                for site in my_data[a].keys():
                    if not my_data[attribute].has_key(site):
                        my_data[attribute][site] = []
                    for i in range(0, len(my_data[a][site])):
                        if len(my_data[attribute][site]) == i:
                            my_data[attribute][site].append(my_data[a][site][i])
                        else:

                            my_data[attribute][site][i] += my_data[a][site][i]





    attributes = my_data.keys()
    # Now, we add the months into one entry
    for a in attributes:
        if a == 'months':
            continue
        sites = my_data[a].keys()
        my_data[a]['TOTAL'] = []
        my_data[a]['All Tier-1s  '] = []
        attributeTotal = 0
        t1Total = 0
        for site in sites:
            siteTotal = 0
            numEntries = len(my_data[a][site])
            # In this case, we count only until the current month
            # if attribute in ('CPU_Pledged_month', 'Disk_Pledged_month', 'Tape_Pledged_month'):
            #    numEntries = CURRENT_MONTH
            for i in range(0, numEntries):
                siteTotal += my_data[a][site][i]
                if len(my_data[a]['TOTAL']) == i :
                    my_data[a]['TOTAL'].append(my_data[a][site][i])
                else:
                    my_data[a]['TOTAL'][i] += my_data[a][site][i]
                if site != 'CH-CERN':
                    if len(my_data[a]['All Tier-1s  ']) == i :
                        my_data[a]['All Tier-1s  '].append(my_data[a][site][i])
                    else:
                        my_data[a]['All Tier-1s  '][i] += my_data[a][site][i]
            # my_data[a][site].append('')
            my_data[a][site].append(siteTotal)
            attributeTotal += siteTotal
            if site != 'CH-CERN':
                t1Total += siteTotal
        # my_data[a]['TOTAL'].append('')
        my_data[a]['TOTAL'].append(attributeTotal)
        my_data[a]['All Tier-1s  '].append(t1Total)


    all_percentages = {
                'disk':{'disk_usage':'installed_disk'},      #'Disk_Pledged_month'},
                'tape':{'tape_used':'installed_x0020_tape'}} #Tape_Pledged_month'}}
    for p in all_percentages:
        attName = all_percentages[p].keys()[0]
        my_data[attName + '_percentage'] = {}
        pledgedAtt = all_percentages[p][attName]
        for site in my_data[attName].keys():
            my_data[attName + '_percentage'][site] = []
            if my_data[attName].has_key(site) and my_data[pledgedAtt].has_key(site):
                for i in range(len(my_data[attName][site])):
                    # my_data[all_percentages[p][attName]][site][i] > 0
                    try:
#                        value = str(int(0.5 + 100. *my_data[attName][site][i] / my_data[pledgedAtt][site][i]/ eff_factor)) + '%'
                        if my_data['efficiency'].has_key(p):
                            eff_factor=my_data['efficiency'][p][i]
                        else:
                            eff_factor=1.
                        value = str(int(0.5 + 100. *my_data[attName][site][i] / my_data[pledgedAtt][site][i]/ eff_factor)) + '%'

                    except:
                        value = '-'
                    my_data[attName + '_percentage'][site].append(value)
    
    return my_data



# @cache_page(60 * 15)
def main(request):


    content = {}
    content['title'] = {'app_id':'acc_report', 'app_title':'Accounting report', 'view_title':'View of the report', 'view_id':'acc_report_id'}
    content['breadcrumbs'] = []
    content['is_top_menu'] = True
    content['my_pages'] = [];
    reqType = request.GET.get('type')

    parameters = checkParameters(request)
    if parameters:
        my_data = getSourceData(parameters['from'], parameters['months'], parameters['federations'], parameters['efficiencyFactors'])
        if not request.GET.get("skipTotals"):
            my_data = calculateTotals(my_data)
    else:
        my_data = {}

    if  reqType == 'json':
        data = json.dumps(my_data)
        return HttpResponse(data, mimetype = 'application/json')
    else:
        content['my_pages'] = createPages(my_data, parameters['from'], parameters['months'], parameters['federations'],
                                          parameters['tables'], parameters['experiments'], parameters['accsum'], parameters['expsum'])


        if reqType == 'pdf':
            result = StringIO.StringIO()
            template = get_template("Accounting_Summary.html")
            context = Context(content)

            html = template.render(context)
            my_object = open("/tmp/my_file", "w")
            my_object.write(html)
            my_object.close()
            pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result, link_callback = fetch_resources,)

            if not pdf.err:
                return HttpResponse(result.getvalue(), mimetype = 'application/pdf')
        elif reqType == 'static':
            return render_to_response("Accounting_Summary.html", content)
        elif reqType == 'pages_json':

            return HttpResponse(json.dumps(content['my_pages']), mimetype = 'application/json')

        else:
            # formatting for the template
            content['sites'] = {}
            # content['multi_table'] = []
            for item in content['my_pages']:
                if 'centre' in item:
                    if item['centre'] in content['sites']:
                        content['sites'][item['centre']].append(item)
                    else:
                        content['sites'][item['centre']] = [item]
                        # content['multi_table'].append([item['centre'], alias])
                else:
                    content['sites'][item['page_type']] = [item]
                    

            content['report_dates'] = getReportDates(parameters)

            return render_to_response("Web_Accounting_Summary.html", content)

def checkParameters(request):
    parameters = {}

    for p in ('from', 'months', 'federations', 'tables', 'graphs', 'experiments', 'accsum', 'expsum'):
        parameters[p] = request.GET.get(p)

    if parameters['tables']:
        parameters['tables'] = parameters['tables'].split(',')
    if parameters['graphs']:
        parameters['graphs'] = parameters['graphs'].split(',')
    if not parameters['from']:
        return False
    try:
        parameters['months'] = int(parameters['months'])
    except:
        parameters['months'] = 12
    parameters['efficiencyFactors'] = {}
    #for f in  EfficiencyFactor.objects.filter(Q(factor_tier = 1)):
    #    parameters['efficiencyFactors'][f.factor_name] = f.factor_value

    return parameters
def contentDefaultValues(parameters):
    content = {}
    content['from'] = parameters['from']
    content['num_months'] = parameters['months']
    content['selectedTables'] = {}
    if parameters['tables']:
        for entry in parameters['tables']:
            content['selectedTables'][str(entry)] = 'SELECTED'

    content['selectedGraphs'] = {}
    if parameters['graphs']:
        for entry in parameters['graphs']:
            content['selectedGraphs'][str(entry)] = 'SELECTED'
    content['selectedExperiments'] = parameters['experiments']
    content['selectedFederations'] = str(parameters['federations'])
    content['selectedAccSum'] = parameters['accsum']
    content['selectedExpSum'] = parameters['expsum']


    return content

def createPlotSeries(plotType, fedName, my_data):
    COLORS = {'ALICE':'#F7F131', 'ATLAS':'#00C8FF', 'CMS':'#90ed7d', 'LHCb':'#BA1111'}

    plots = []
    if plotType == 'cputime':
        for exp in ('ALICE', 'ATLAS', 'CMS', 'LHCb'):
            plots.append({  'type': 'column',
                           'name': exp,
                           'data':  map(lambda x: int(x / 1000) , my_data[exp + '_cpu_usage'][fedName][:-1]),
                           'color': COLORS[exp],
                          })
        plots.append({
                    'type': 'spline',
                    'name': 'MoU commitment',
                    'data': map(lambda x: x*24 / 1000 , my_data['CPU_Pledged_month'][fedName][:-1]),
                    'color': '#8085e9'
                    })
    if plotType == 'walltime':
        for exp in ('ALICE', 'ATLAS', 'CMS', 'LHCb'):
            plots.append({
                       'type': 'column',
                       'name': exp,
                       'data': map(lambda x: int(x / 1000) , my_data[exp + '_wall_time'][fedName][:-1]),
                       'color': COLORS[exp],
                      })
        plots.append({
                    'type': 'spline',
                    'name': 'MoU commitment',
                    'data': map(lambda x: x*24 / 1000 , my_data['CPU_Pledged_month'][fedName][:-1]),
                    'color': '#8085e9'
                   })
    if plotType == 'efficiency':
        for exp in ('ALICE', 'ATLAS', 'CMS', 'LHCb'):
            data = []
            for i in range(0, len(my_data[exp + '_cpu_usage'][fedName]) - 1):
                try:
                    value = my_data[exp + '_cpu_usage'][fedName][i] / my_data[exp + '_wall_time'][fedName][i] * 100
                except:
                    value = 0
                data.append(value)
            plots.append({'type': 'spline',
                           'name': exp,
                           'data': data,
                           'color': COLORS[exp],
                          })
    if ( plotType == 'disk' or plotType == 'tape'):
        fieldNames= ['installed_disk', 'Disk_Pledged_month']
        if plotType=='tape':
            fieldNames=['installed_x0020_tape', 'Tape_Pledged_month']

        for exp in ('ALICE', 'ATLAS', 'CMS', 'LHCb'):
            fieldName=exp + '_disk_usage'
            if (plotType=='tape'):
                fieldName='tape_used_' + exp
            plots.append({'type': 'column',
                           'name': exp,
                           'data': my_data[fieldName][fedName][:-1],
                           'color': COLORS[exp],
                          })
        # creating disk storage plot
        plots.append({
                           'type': 'spline',
                           'name': 'Installed Capacity',
                           'data': my_data[fieldNames[0]][fedName][:-1],
                           'color': '#F78E16'
                          })
        plots.append({
                           'type': 'spline',
                           'name': 'Mou commitment',
                           'data':my_data[fieldNames[1]][fedName][:-1],
                           'color': '#8085e9'
                          },)

    return plots

def contentForPlots(parameters, content, my_data):
    content['plotMonths'] = '[' + ','.join([ "'" + a + "'"  for a in calculateMonthNames(parameters['from'], parameters['months']) ]) + ']'

    graphs = parameters['graphs']
    if not graphs:
        graphs = []
    plot_info = {'cputime':{'title':'CPU Time Delivered', 'yAxis':'KHS06-hours', },

                  'walltime':{'title':'Wall-clock Time Delivered', 'yAxis':'KHS06-hours * #cores',
                              'series':"{'color': '#77F131', 'data': [868.78399999999999, 974.07600000000002, 1475.1179999999999, 1560.559, 2051.8490000000002, 1311.383, 1246.2850000000001, 1233.433, 1257.018, 1134.797, 1136.8989999999999, 951.875], 'type': 'column', 'name': 'ALICE'},"},
                  'efficiency':{'title':'Ratio of CPU: Wall-clock Times', 'yAxis':'%',
                                'series':"{'color': '#777731', 'data': [868.78399999999999, 974.07600000000002, 1475.1179999999999, 1560.559, 2051.8490000000002, 1311.383, 1246.2850000000001, 1233.433, 1257.018, 1134.797, 1136.8989999999999, 951.875], 'type': 'column', 'name': 'ALICE'},"},
                  'disk':{'title':'Disk Storage Used', 'yAxis':'TeraBytes',
                                'series':"{'color': '#777731', 'data': [868.78399999999999, 974.07600000000002, 1475.1179999999999, 1560.559, 2051.8490000000002, 1311.383, 1246.2850000000001, 1233.433, 1257.018, 1134.797, 1136.8989999999999, 951.875], 'type': 'column', 'name': 'ALICE'},"},
                  'tape':{'title':'Tape Storage Used', 'yAxis':'TeraBytes',
                                'series':"{'color': '#777731', 'data': [868.78399999999999, 974.07600000000002, 1475.1179999999999, 1560.559, 2051.8490000000002, 1311.383, 1246.2850000000001, 1233.433, 1257.018, 1134.797, 1136.8989999999999, 951.875], 'type': 'column', 'name': 'ALICE'},"}
                  }
    if not parameters['federations']:
        return
    fedNames = parameters['federations'].split(',')
    for entry in graphs:
        if entry == 'nographs':
            continue
        content['selectedGraphs'][entry] = plot_info[entry]
        content['selectedGraphs'][entry]['series'] = {}
        for fed in fedNames:
            keyName = str(fed)
            if keyName == 'All_Tier-1s_and_CERN':
                keyName = 'TOTAL'
            elif keyName == 'All_Tier-1s__':
                keyName = 'All Tier-1s  '

#            if fed == 'TOTAL':
#                displayName = 'CERN_and_Tier-1s'
#            if parameters['federations'] and displayName not in parameters['federations']:
#                continue
            content['selectedGraphs'][entry]['series'][fed] = createPlotSeries(entry, keyName, my_data)

def createCustomised(parameters):
    content = contentDefaultValues(parameters)

    my_data = getSourceData(parameters['from'], parameters['months'], parameters['federations'], parameters['efficiencyFactors'])
    my_data = calculateTotals(my_data)
    my_pages = createPages(my_data, parameters['from'], parameters['months'], parameters['federations'],
                           parameters['tables'], parameters['experiments'], parameters['accsum'], parameters['expsum'])  # year[-2:])

    contentForPlots(parameters, content, my_data)

    content['federations'] = {}
    for p in my_pages:
        if not content['federations'].has_key(p['centre']):
            content['federations'][p['centre']] = []
        content['federations'][p['centre']].append(p)
        # if not p['centre'] in siteNames:
        #    siteNames.append(p['centre'])
    siteNames = content['federations'].keys()
    siteNames.sort()

    content['sortedTabs'] = siteNames
    return content

def customised(request):
    content = {}
    # Trying to get the data from the cache

    parameters = checkParameters(request)

    if parameters:

        content = createCustomised(parameters)

    content['title'] = {'app_id':'acc_report', 'app_title':'Accounting report', 'view_title':'WLCG Accounting', 'view_id':'acc_report_id'}
    content['breadcrumbs'] = []
    content['is_top_menu'] = True
    content['Experiments'] = VO_NAMES

    content['federationNames'] = ['All Tier-1s + CERN', 'All Tier-1s  '] + getFedNames()
    content['report_dates'] = getReportDates(parameters)

#    content['efficiency_string'] = getEfficiencyFactors(parameters)
#    content['efficiency_dict'] = getEfficiencyDictionary(parameters)

    return render_to_response("rebus-tier1/Web_Accounting_Summary.html", content, context_instance=RequestContext(request))

def getReportDates(parameters):
    try:
      months =['January', "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
      (start, year) = parameters['from'].split(' ', 2);
      start_number= months.index(start)
      end_number = ( start_number + parameters["months"] -1 ) % 12
    
      return start + " - " + months[end_number]
    except:
      return " no dates"
  
def getFedNames():
    #fed_names = [f.long_name for f in Federation.objects.filter(Q(tier = 0) | Q(tier = 1))]
    fed_names = FEDERATIONS
    fed_names.sort()
    return fed_names

def efficiency(request):
    content = {}
    content['title'] = {'app_id':'acc_report', 'app_title':'Accounting report', 'view_title':'View of the report', 'view_id':'acc_report_id'}
    return render_to_response("rebus-tier1/Pledge_Table.html", content)



def browse(parameters):
    content = {}
    content['title'] = {'app_id':'acc_report', 'app_title':'Accounting report', 'view_title':'View of the report', 'view_id':'acc_report_id'}
    content['breadcrumbs'] = []
    content['is_top_menu'] = True

    return render_to_response("rebus-tier1/Browse_Reports.html", content)
