import urllib
from BeautifulSoup import *

numlist = list()

html = urllib.urlopen('http://python-data.dr-chuck.net/comments_188865.html').read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    num = tag.text
    numf = float(num)
    numlist.append(numf)

print 'Sum:', sum(numlist)