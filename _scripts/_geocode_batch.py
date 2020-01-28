import csv
import sys
import requests
from io import StringIO

BASE_URL = 'https://geocoding.geo.census.gov/geocoder/locations/addressbatch'


with open('data/pharma-locations-parsed.csv','rb') as infile:
    with open('data/pharma-batch-geo.csv','wb') as outfile:
        form_data = {
            'benchmark': 'Public_AR_Current',
        }
        file = {'addressFile':('pharma-locations-parsed.csv',infile, 'application/octet-stream',{})}
        
        r = requests.post(BASE_URL,data=form_data,files=file)
        outfile.write(r.content)