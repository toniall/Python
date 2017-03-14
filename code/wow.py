import urllib
import json

url = 'http://auction-api-us.worldofwarcraft.com/auction-data/4923213e5eb3ec3b7e03d22b632bda36/auctions.json'

print 'Retrieving: ', url

uh = urllib.urlopen(url)
data = uh.read()

print 'Retrieved: ',len(data),' characters'


js = json.loads(str(data))

print json.dumps(js, indent=4)