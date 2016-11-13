from bs4 import BeautifulSoup
import urllib

def get_summaries(bill_url):
    """Returns each summary in dictionary with the values in keys"""
    summaries = {}
    r = urllib.urlopen(bill_url)
    soup = BeautifulSoup(r, 'html.parser')

    for p in (soup.find_all('p')):
        try:
            key = int(p.prettify()[11:12])
            value =  p.get_text()
            summaries[key] = value
        except:
            #print p.prettify()[11:12]
            pass
    if not bool(summaries):
        full_sum = soup.find("div", {"id": "libraryofcongress"})
        [s.extract() for s in full_sum('script')]
        count = 0
        result = []
        length = len(soup.find_all('p'))-20
        for p in (soup.find_all('p')):
            if count >= 7 and count <= length: 
                result.append(p.get_text())
            count += 1            
            #print p.get_text()
        summaries[0] = "".join(result)
        if summaries[0] == "":
            summaries[0] = "N/A"
    return summaries


