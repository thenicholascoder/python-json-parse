# example type Ann Arbor, MI

#import urllib
import urllib.request, urllib.parse, urllib.error

#import json
import json

#url as a string
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

#indefinite loop, true means this will run only until until it breaks
while True:

	# you will write the location of the address
    address = input('Enter location: ')
    # example you hit Ann Arbor, MI

    # if i hit enter , it will get out of the loop
    if len(address) < 1: break

    # will get serviceurl
    # will transform this urllib.parse.urlencode({'address': address})
    # into address=Ann+Arbor%C+MI
    # concatenate into
    # https://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%C+MI
    url = serviceurl + urllib.parse.urlencode({'address': address})
    
    # print Retrieving url
    print('Retrieving', url)

   	# file handler
    uh = urllib.request.urlopen(url, context=ctx)

    # pull all the entire doc {}[] , then decode utf8 to string
    data = uh.read().decode()

    # this will print Retrieved, len(data) characters
    print('Retrieved', len(data), 'characters')

    # try this first, if it blows up then run except
    try:

    	# json.load string from DATA and return a dictionary 
        js = json.loads(data)

    except:

    	# or elseit will have a value of js = None
        js = None

    # filter if JS is false, if status key is not in the js dictionary or status key is not equal to OK value
    # if not js = if we got nothing
    # status not in js = if status not in dictionary
    # status != OK = if status is not equal to okay
    if not js or 'status' not in js or js['status'] != 'OK':

    	# print failed
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # this will pretty print it with indent of 4
    # this will look like how you see a json file
    print(json.dumps(js, indent=4))

    # walking down the data to the child lat and lng value 
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']

    # print the result lat and lng
    print('lat', lat, 'lng', lng)

    # walk to formatted_address value
    location = js['results'][0]['formatted_address']

    #print location
    print(location)