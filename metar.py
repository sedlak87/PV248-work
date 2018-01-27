import requests
from lxml import etree

r = requests.get("https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=LKTB,%20PHNL&hoursBeforeNow=2")

tree = etree.fromstring(r.content)

for e in tree.findall('.//data/METAR'):
        time = e.find('./observation_time').text
        temp = e.find('./temp_c').text
        print('{} - {}'.format(time, temp))
