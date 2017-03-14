import json

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'auctions.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)
print json_data

for entry in json_data:
    
    name = entry[2];
    title = entry[3];

    print name, title