import csv
import requests

BASE_URL = 'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress'
params = {
    'address':'',
    'benchmark':'Public_AR_Current',
    'format':'json'
}

with open('pharma-locations.csv','r') as data_file:
    with open('pharma-locations-geo.csv','w') as output_file:
        csv_reader = csv.reader(data_file)
        headers = next(csv_reader,None)
        new_headers = headers + ['latitude','longitude']

        csv_writer = csv.DictWriter(output_file,fieldnames=new_headers)
        csv_writer.writeheader()

        row_count = 0

        for row in csv_reader:
            obj = {}
            for x in range(len(headers)):
                obj[headers[x]] = row[x]
            params['address'] = obj['address']

            req = requests.get(BASE_URL,params=params)
            matches = req.json()['result']['addressMatches']
            if len(matches) > 0:
                print(f"✅ {obj['address']}")
                location = matches[0]
                lat = matches[0]['coordinates']['y']
                lon = matches[0]['coordinates']['x']
                obj['latitude'] = lat
                obj['longitude'] = lon

            else:
                print(f"❌ {obj['address']}")
                obj['latitude'] = ''
                obj['longitude'] = ''

            csv_writer.writerow(obj)

            # if row_count > 20:
            #     break
            row_count += 1