
import re
hand = open('/Users/Casa/Desktop/Python/code/regex_sum_188860.txt')
numsum=0
count=0
numlist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)',line)

    stuffl = len(stuff)
    
    if stuffl < 1: continue
    #print stuffl
    #print stuff
    if stuffl >= 1:
        for ind in stuff:
            num = float(ind)
            #count = count +1
            #numsum = numsum + num
            numlist.append(num)
#print count
#print numsum

print 'Sum:', sum(numlist)