import csv
import sys
import requests
from io import StringIO

BASE_URL = 'https://geocoding.geo.census.gov/geocoder/locations/addressbatch'


with open('pharma-locations-parsed.csv','rb') as infile:
    with open('pharma-batch-geo.csv','wb') as outfile:
        form_data = {
            'benchmark': 'Public_AR_Current',
        }
        file = {'addressFile':('pharma-locations-parsed.csv',infile, 'application/octet-stream',{})}
        # csv_reader = csv.reader(infile)
        # headers = next(csv_reader,None)

        # f = StringIO()
        # mem_writer = csv.DictWriter(f, fieldnames=headers)
        # mem_writer.writeheader()
        
        # for row in csv_reader:
        #     obj = {}
        #     for i in range(len(headers)):
        #         obj[headers[i]] = row[i]
        #     print(obj)
        #     mem_writer.writerow(row)
        r = requests.post(BASE_URL,data=form_data,files=file)
        outfile.write(r.content)