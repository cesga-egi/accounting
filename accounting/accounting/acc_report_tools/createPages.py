from staticVariables import VO_NAMES

def times24(x):
    return x*24;

def createEmptyPage(allPages, siteName, from_date, number_months):
    allPages.append({'page_title':'', 'centre':siteName, 'month':from_date,
                     'pledges_table' : [],
                     'dates':calculateMonthNames(from_date, number_months),
                     'tables': [] })
# def createPages(my_data, current_month, month_name, yearHeader = '14', sitesToCreate = "", pagesToCreate = ""):
def createPages(my_data, from_date, number_months, sitesToCreate = "", pagesToCreate = "", experimentsToCreate = "", accSum = None, expSum = None, metricDays = None):

    allPages = []
    if accSum:
        createSummaryPage(allPages, my_data, from_date, number_months, metricDays)
    if expSum:
        createSummaryExpPage(allPages, my_data, from_date, number_months, metricDays)

    federations = my_data['CPU_Pledged'].keys()


    for  fedName  in federations:
        if sitesToCreate:
            if fedName == 'TOTAL' :
                if "All_Tier-1s_and_CERN" not in sitesToCreate:
                    continue
            elif fedName == 'All Tier-1s  ':
                if "All_Tier-1s__" not in sitesToCreate:
                    continue
            elif fedName not in sitesToCreate:
                continue
        if pagesToCreate and 'notables' in pagesToCreate:
            createEmptyPage(allPages, fedName, from_date, number_months)
            continue
        if pagesToCreate and 'cpu' in pagesToCreate:
            createCPUPage(allPages, my_data, fedName, from_date, number_months, experimentsToCreate, metricDays)
        if pagesToCreate and  ('disk' in pagesToCreate or 'tape' in pagesToCreate):
            createStoragePage(allPages, my_data, fedName, from_date, number_months, pagesToCreate, experimentsToCreate, metricDays)
    return allPages

def createSummaryExpPage(allPages, my_data, current_month, month_name, metricDays):

    federations = my_data['CPU_Pledged'].keys()
    federations.sort()
    my_experiments = {}
    for exp in VO_NAMES:
        my_experiments[exp] = {'name':exp, 'sites':[]}
        my_total = []
        for fedName in federations:

            newName = fedName
            # This is to put the total at the top
            if fedName == 'TOTAL':
                my_total = [my_data[exp + '_wall_time'][fedName][-1], '100%', my_data[exp + '_disk_usage'][fedName][-2], '100%',
                            my_data['tape_used_' + exp][fedName][-2], '100%']
                continue
            disk_percentage = "n/a"
            if  my_data[exp + '_disk_usage']['TOTAL'][-2] > 0:
                disk_percentage = "%.0f%%" % (100. * my_data[exp + '_disk_usage'][fedName][-2] / my_data[exp + '_disk_usage']['TOTAL'][-2])
            tape_percentage = "n/a"
            if my_data['tape_used_' + exp]['TOTAL'][-2]>0:
                tape_percentage = "%.0f%%" % (100. * my_data['tape_used_' + exp][fedName][-2] / my_data['tape_used_' + exp]['TOTAL'][-2])
            my_experiments[exp]['sites'].append({'month':month_name,
                                                 'name':newName, 'values':[
                                                                            my_data[exp + '_wall_time'][fedName][-1],
                                                     "%.0f%%" % (100. * my_data[exp + '_wall_time'][fedName][-1] / my_data[exp + '_wall_time']['TOTAL'][-1]),
                                                     my_data[exp + '_disk_usage'][fedName][-2],
                                                     disk_percentage,
                                                     my_data['tape_used_' + exp][fedName][-2],
                                                     tape_percentage,
                                                     ]})
        my_experiments[exp]['sites'].append({'month':month_name, 'name':'TOTAL', 'values':my_total})



    allPages.append({'page_type': 'SummaryExp',
                     'exp1':my_experiments['ALICE'],
                     'exp2':my_experiments['CMS'],
                     'exp3':my_experiments['ATLAS'],
                     'exp4':my_experiments['LHCb'],
                     'centre':' Experiment Summary Page',
                     'page_title':' Experiment summary',
                      })
def createSummaryPage(allPages, my_data, from_date, number_months, metricDays):
    federations = my_data['CPU_Pledged'].keys()
    federations.sort()
    my_sites = []
    first = 1
    for  fedName in federations + ['TOTAL']:
        if fedName=='TOTAL' and first==1: 
            first = 0
            continue
        #assert False, locals()
        my_sites.append({'name':fedName,
                         'values':[my_data['wall_time'][fedName][-1],
                                   colorCodeSummary(my_data['wall_time'][fedName][-1] , 24 * my_data['CPU_Pledged_month'][fedName][-1]),
                                   # Now, the disk
                                   my_data['disk_usage'][fedName][-1],
                                   colorCodeSummary(my_data['disk_usage'][fedName][-1] , my_data['installed_disk'][fedName][-1]),
                                   colorCodeSummary(my_data['disk_usage'][fedName][-1] , my_data['Disk_Pledged_month'][fedName][-1]),
                                   my_data['disk_usage'][fedName][-2],
                                   colorCodeSummary(my_data['disk_usage'][fedName][-2] , my_data['installed_disk'][fedName][-2]),
                                    colorCodeSummary(my_data['disk_usage'][fedName][-2] , my_data['Disk_Pledged_month'][fedName][-2]),
                                    colorCodeSummary(my_data['installed_disk'][fedName][-2] , my_data['Disk_Pledged_month'][fedName][-2]),
                                   # Finally, tape
                                   my_data['tape_used'][fedName][-1],
                                   colorCodeSummary(my_data['tape_used'][fedName][-1] , my_data['installed_x0020_tape'][fedName][-1]),
                                   colorCodeSummary(my_data['tape_used'][fedName][-1] , my_data['Tape_Pledged_month'][fedName][-1]),
                                   my_data['tape_used'][fedName][-2],
                                   colorCodeSummary(my_data['tape_used'][fedName][-2] , my_data['installed_x0020_tape'][fedName][-2]),
                                   colorCodeSummary(my_data['tape_used'][fedName][-2] , my_data['Tape_Pledged_month'][fedName][-2]),
                                   colorCodeSummary(my_data['installed_x0020_tape'][fedName][-2] , my_data['Tape_Pledged_month'][fedName][-2]),
                                                        ]})

    my_experiments = []
    total = {}

    for attribute in ("_wall_time", '_disk_usage', 'tape_used_'):
        total[attribute] = 0
        for exp in VO_NAMES:
            fieldName = exp + attribute
            if attribute == 'tape_used_':
                fieldName = attribute + exp
            c=-2;
            if attribute == '_wall_time':
                c=-1
            total[attribute] += my_data[fieldName]['TOTAL'][c]
   

    for exp in VO_NAMES:
        my_experiments.append({'name':exp, 'values':[ my_data[exp + '_wall_time']['TOTAL'][-1],
                                                     "%.0f%%" % (100. * my_data[exp + '_wall_time']['TOTAL'][-1] / total['_wall_time']) ,
                                                     my_data[exp + '_disk_usage']['TOTAL'][-2],
                                                     "%.0f%%" % (100. * my_data[exp + '_disk_usage']['TOTAL'][-2] / total['_disk_usage']) ,
                                                     my_data['tape_used_' + exp]['TOTAL'][-2],
                                                     "%.0f%%" % (100. * my_data['tape_used_' + exp]['TOTAL'][-2] / total['tape_used_']) , ]})

    my_experiments.append({'name':'TOTAL', 'values':[my_data['wall_time']['TOTAL'][-1], "100%", total['_disk_usage'], "100%", total['tape_used_'], "100%"]})

    allPages.append({'page_type': 'Summary',
                     'sites':my_sites,
                     'experiments':my_experiments,
                     'centre':' Accounting Summary Page',
                     'page_title':'SUMMARY TITLE',
                      })
def colorCodeSummary(top, bottom):
    if bottom == 0:
        return '<font color="red"> n/a </font>'
    num = int( 0.5 + 100. * top / bottom);
    if num < 50:
        return '<font color="red">' + str(num) + ' %</font>';
    if num > 90:
        return '<font color="green">' + str(num) + ' %</font>';
    return str(num) + '%'

def createStoragePage(allPages, my_data, pageEntry, from_date, number_months, pagesToCreate, experimentsToCreate, metricDays):

    to_return = {}
    to_return['Disk Space'] = []
    to_return['Tape Space'] = []


    for exp in VO_NAMES:
        if experimentsToCreate and exp not in experimentsToCreate:
            continue
        to_return['Disk Space'].append ({'row_title':exp, 'row_content':[ {'row_title':'allocated', 'row_content':my_data[exp + '_disk_allocated' ][pageEntry] + ['']},
                                                                         {'row_title':'used' , 'row_content':my_data[ exp + '_disk_usage' ][pageEntry] + ['']},
                                                                       ]})

        to_return['Tape Space'].append ({'row_title':exp, 'row_colspan':2, 'row_content':[ { 'row_content':my_data[ 'tape_used_' + exp ][pageEntry] + ['']}]})

    disk_allocated = str(100 * int(my_data['disk_allocated' ][pageEntry][-1]) / int(my_data['Disk_Pledged_month'][pageEntry][-1])) + '%'
    disk_used = str(100 * int(my_data['disk_usage' ][pageEntry][-1]) / int(my_data['Disk_Pledged_month'][pageEntry][-1])) + '%'
    to_return['Disk Space'].append ({'row_title':'TOTAL', 'row_content':[ {'row_title':'allocated', 'row_content':my_data['disk_allocated' ][pageEntry] + [disk_allocated]},
                                                                         {'row_title':'used' , 'row_content':my_data['disk_usage' ][pageEntry] + [disk_used]},
                                                                       ]})

    to_return['Disk Space'].append ({'row_title':'installed capacity **', 'row_colspan':2,
                                    'row_content':[{'row_content':my_data['installed_disk'][pageEntry] + ['']}]})
    to_return['Disk Space'].append ({'row_title':'MoU pledge *', 'row_content':[{'row_title':' ', 'row_content':my_data['Disk_Pledged_month'][pageEntry] + ['']},
                                                                               ]})
    tape_used = str(100 * int(my_data['tape_used' ][pageEntry][-1]) / int(my_data['Tape_Pledged_month'][pageEntry][-1])) + '%'

    to_return['Tape Space'].append ({'row_title':'TOTAL ***', 'row_colspan':2, 'row_content':[ { 'row_content':my_data[ 'tape_used' ][pageEntry] + [tape_used]}]})
    to_return['Tape Space'].append ({'row_title':'installed capacity **', 'row_colspan':2,
                                    'row_content':[{'row_content':my_data['installed_x0020_tape'][pageEntry] + [''] }]})
    to_return['Tape Space'].append ({'row_title':'MoU pledge *', 'row_content':[{'row_title':' ', 'row_content':my_data['Tape_Pledged_month'][pageEntry] + [''] },
                                                                               ]})
    siteName = pageEntry
    if pageEntry == 'TOTAL':
        siteName = 'All Tier-1s + CERN'
    if 'disk' in pagesToCreate:
        allPages.append({'page_title':'Disk Space - TBytes', 'centre':siteName, 'month':from_date,
                         'pledges_table' : getPledgeTable(from_date, number_months, siteName, my_data),
                         'dates':calculateMonthNames(from_date, number_months),
                         'tables': [{'table_blocks':[{'block_title':'', 'block_rowspan':14 , 'rows': to_return['Disk Space']  }, ], } ]
                           })
    if 'tape' in pagesToCreate:
        allPages.append({'page_title':'Tape Space Used - TBytes', 'centre':siteName, 'month':from_date,
            'pledges_table' : getPledgeTable(from_date, number_months, siteName, my_data),
            'dates':calculateMonthNames(from_date, number_months),
                                'tables': [{'table_blocks':[{'block_title':'', 'block_rowspan':8 , 'rows': to_return['Tape Space']}]  # Tape Space Used - TBytes
                                            }]
                           })
def getPledgeTable(from_date, number_months, siteName, my_data):
    if siteName == 'All Tier-1s + CERN':
        siteName = 'TOTAL';
    return  [{'title': 'MoU pledges', 'values':getPledgesDates(from_date, number_months)},
                               {'title':'CPU (HS06-years)', 'values': map(times24, my_data['CPU_Pledged'][siteName][:-1])},
                               {'title':'Disk (Tbytes)', 'values':my_data['Disk_Pledged'][siteName][:-1]},
                               {'title':'Tape (Tbytes)', 'values':my_data['Tape_Pledged'][siteName][:-1]}, ]
def getPledgesDates(fromDate, number_months):
    month_name, year = fromDate.split(' ')
    month_name = month_name[0:3]
    my_dates = []
    entries = 0
    all_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    my_year = int(year) - 2000
    if month_name in ('Jan', 'Feb', 'Mar'):
        my_year = my_year - 1
        number_months += 9 +  all_months.index(month_name)  
    else:
        # We have to get some more months. If we are in August, and ask for 12 months, that will require the pledges of the next year
        number_months += all_months.index(month_name) - 3
    while number_months > 0:
        my_dates.append('apr-%i\nmar-%i' % (my_year, my_year + 1))
        my_year += 1
        number_months -= 12

    return my_dates


def createCPUPage(allPages, my_data, pageEntry, from_date, number_months, experimentsToCreate, metricDays):

    to_return = {'CPU Grid':[], 'CPU Non-Grid':[], 'CPU Total':[], 'MoU':[]}
    all_blocks = {'CPU Grid': 'grid_', 'CPU Non-Grid': 'non_grid_', 'CPU Total': ''}
    period = 'Days' if metricDays else 'Hours'
    order = 0
    for block in all_blocks.keys():
        prefix = all_blocks[block]
        for exp in VO_NAMES:
            if experimentsToCreate and exp not in experimentsToCreate:
                continue
            to_return[block].append ({'row_title':exp, 'row_content':[{'row_title':'', 'row_content':my_data[prefix + exp + '_wall_time' ][pageEntry] + ['']},
                                                                       ]})
        if not experimentsToCreate or 'total' in experimentsToCreate:
#            f = str(100 * int (my_data[prefix + 'cpu_usage' ][pageEntry][-1]) / (24 * int(my_data['CPU_Pledged_month'][pageEntry][-1]))) + '%'
            g = str(100 * int (my_data[prefix + 'wall_time' ][pageEntry][-1]) / (24 * int(my_data['CPU_Pledged_month'][pageEntry][-1]))) + '%'
            to_return[block].append ({'row_title':'TOTAL', 'row_content':[ {'row_title':'', 'row_content':my_data[prefix + 'wall_time'][pageEntry] + [g]},
                                                                       ]})

    to_return['MoU'].append ({'row_title':'MoU pledge ***', 'row_content':[{'row_content': map(times24, my_data['CPU_Pledged_month'][pageEntry]) + [''] }]})



    siteName = pageEntry
    if pageEntry == 'TOTAL':
        siteName = 'All Tier-1s + CERN'
    allPages.append({'page_title':'Wallclock Work in HEPSPEC06 '+period, 'centre':siteName, 'month':from_date,
                     'pledges_table' :getPledgeTable(from_date, number_months, siteName, my_data),
                     'dates':calculateMonthNames(from_date, number_months),
                                 'tables': [{'table_blocks':[
                                                 {'block_title':'Global**', 'rows': to_return['CPU Grid']  },
                                                { 'block_title':'Local*', 'rows':to_return['CPU Non-Grid']},
                                                { 'block_title':'Total', 'block_rowspan':10 , 'rows':to_return['CPU Total']},
                                                { 'block_title':'', 'block_rowspan':3 , 'rows':to_return['MoU']},
                                                ], }],
                           })
def calculateMonthNames(from_date, number_months):
    MONTH_NAME = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    all_months = []
    (month, year) = from_date.split(' ')
    month = month[0:3]
    while number_months > 0:
        all_months += [str (month + ' ' + year)]
        if month == 'Dec':
            year = str(int(year) + 1)
            month = 'Jan'
        else:
            month = MONTH_NAME[MONTH_NAME.index(month[0:3]) + 1]
        number_months -= 1

    return all_months

