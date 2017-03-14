import json

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'roster_data_sample.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)
for entry in json_data:
    
    name = entry[0];
    title = entry[1];

    print name, title