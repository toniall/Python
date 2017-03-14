import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = "Universidad de Buenos Aires"

url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url

uh = urllib.urlopen(url)
data = uh.read()

js = json.loads(str(data))

place_id = js['results'][0]['place_id']
print place_id