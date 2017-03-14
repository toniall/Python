import urllib
from BeautifulSoup import *
urllist = list()


#url = raw_input('Enter URL: ')
url = 'http://python-data.dr-chuck.net/known_by_Fatimah.html '
#count = raw_input('Enter count: ')
#position = raw_input('Enter position: ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
urllist.append(url)


# Retrieve all of the anchor tags
tags = soup('a')
#for tag in tags:
#for tag in tags:
#       print tag.get('href', None)
url1 = tags[17].get('href', None)
print url
print url1

html = urllib.urlopen(url1).read()
soup = BeautifulSoup(html)
urllist.append(url1)
# Retrieve all of the anchor tags
tags = soup('a')
#for tag in tags:
url2 = tags[17].get('href', None)
print url2

html = urllib.urlopen(url2).read()
soup = BeautifulSoup(html)
urllist.append(url2)
# Retrieve all of the anchor tags
tags = soup('a')
#for tag in tags:
url3 = tags[17].get('href', None)
print url3


html = urllib.urlopen(url3).read()
soup = BeautifulSoup(html)
urllist.append(url3)
# Retrieve all of the anchor tags
tags = soup('a')
#for tag in tags:
url4 = tags[17].get('href', None)
print url4

html = urllib.urlopen(url4).read()
soup = BeautifulSoup(html)
urllist.append(url4)
# Retrieve all of the anchor tags
tags = soup('a')
#for tag in tags:
url5 = tags[17].get('href', None)
print url5

html = urllib.urlopen(url5).read()
soup = BeautifulSoup(html)
urllist.append(url5)
# Retrieve all of the anchor tags
tags = soup('a')
#for tag in tags:
url6 = tags[17].get('href', None)
print url6

html = urllib.urlopen(url6).read()
soup = BeautifulSoup(html)
urllist.append(url6)
# Retrieve all of the anchor tags
tags = soup('a')
#for tag in tags:
url7 = tags[17].get('href', None)
print url7
urllist.append(url7)

print urllist