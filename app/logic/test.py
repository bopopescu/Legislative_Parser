import urllib, json
url = "https://www.govtrack.us/api/v2/bill/341073/"
response = urllib.urlopen(url)
data = json.loads(response.read())

print data['number']
print data['congress']
print data['bill_type_label']

print "\n-------\n"

for x in data:
    print x
