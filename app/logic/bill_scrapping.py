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
            summaries["key"] = value
        except:
            pass
    return summaries
