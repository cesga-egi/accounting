import urllib
import json
from django.conf import settings

def getSourceData(fromDate, months, sites, efficiencyFactors, metricDays):
    my_data = getUsageData(fromDate, months, sites, metricDays)
    return my_data

def getUsageData(fromDate, months, sites, metricDays):
    try:
        monthName, year = fromDate.split(' ')
    except:
        monthName, year = fromDate.split('%20')
    monthName = monthName[0:3]
    all_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthNumber = str(all_months.index(monthName) + 1)
    url = settings.SUPPORT_SERVER + '/reptier1.php?sYear=' + year + '&sMonth=' + monthNumber + '&Months=' + str(months) + '&metricDays=' + str(metricDays)
    data = urllib.urlopen(url)
    data_dict = json.load(data)
    return data_dict
