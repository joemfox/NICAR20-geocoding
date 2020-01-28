import csv
import usaddress

with open('data/pharma-locations.csv','r') as infile:
    with open('data/pharma-locations-parsed.csv','w') as outfile:
        csv_reader = csv.reader(infile)
        headers = next(csv_reader,None)
        new_headers = ['id','street','city','state','zip']
        csv_writer = csv.DictWriter(outfile,fieldnames=new_headers)
        csv_writer.writeheader()

        row_count = 0
        for row in csv_reader:
            obj = {}
            new_obj = {}
            address = []
            for i in range(len(headers)):
                obj[headers[i]] = row[i]
            
            parsed_addr = usaddress.parse(obj['address'])
            
            # we need street, city, state, zip
            streetParts = [
                'AddressNumber',
                'StreetNamePreDirectional',
                'StreetNamePreModifier',
                'StreetNamePreType',
                'StreetName',
                'StreetNamePostType',
                'StreetNamePostModifier',
                'StreetNamePostDirectional',
            ]
            otherParts =  [
                    'PlaceName',
                    'StateName',
                    'ZipCode'
                ]
            addressParts = streetParts + otherParts
               
            for bit in parsed_addr:
                if bit[1] in addressParts:
                    address.append(bit)


            streetAddress = ' '.join([bit[0] for bit in list(filter(lambda x: x[1] in streetParts,address))])
            city = ' '.join([bit[0] for bit in list(filter(lambda x: x[1] == 'PlaceName',address))])
            state = ' '.join([bit[0] for bit in list(filter(lambda x: x[1] == 'StateName',address))])
            zipCode = ' '.join([bit[0] for bit in list(filter(lambda x: x[1] == 'ZipCode',address))])
            print(streetAddress, city, state, zipCode)
            
            new_obj['id'] = row_count
            new_obj['street'] = streetAddress
            new_obj['city'] = city
            new_obj['state'] = state
            new_obj['zip'] = zipCode
            csv_writer.writerow(new_obj)

            # if(row_count > 20):
            #     break
            row_count += 1
        