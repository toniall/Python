import urllib
from BeautifulSoup import *
import re
urllist = list()

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
count = int(count)
count = count + 1
position = raw_input('Enter position: ')
index = int(position) - 1
count = int(count)

for counts in range(count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    urllist.append(url)
    print 'Retrieving: ',url
    tags = soup('a')
    url = tags[index].get('href', None)

print urllist[count-1]




