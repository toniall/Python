import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
counts = dict()
for line in fhand:
    print line
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print counts