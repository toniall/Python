import urllib
import json

counts = 0

url = 'http://python-data.dr-chuck.net/comments_188866.json'

print 'Retrieving: ', url

uh = urllib.urlopen(url)
data = uh.read()
js = json.loads(str(data))

print 'Retrieved: ',len(data),' characters'

for item in js["comments"]:
    count = int(item["count"])
    counts = counts + count

print counts