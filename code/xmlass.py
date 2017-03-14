import urllib
import xml.etree.ElementTree as ET

sumCounts = 0

serviceurl = 'http://python-data.dr-chuck.net/comments_188862.xml'
uh = urllib.urlopen(serviceurl)
data = uh.read()

commentinfo = ET.fromstring(data)

counts = commentinfo.findall('comments/comment')

for item in counts:
    sumCount = int(item.find('count').text)
    sumCounts = sumCounts + sumCount

print sumCounts