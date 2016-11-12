import urllib, json
url = "https://www.govtrack.us/api/v2/bill?congress=114"
response = urllib.urlopen(url)
data = json.loads(response.read())

for x in data['objects']:
    if x['is_alive']:
        print x['title_without_number']
        print x['id']
