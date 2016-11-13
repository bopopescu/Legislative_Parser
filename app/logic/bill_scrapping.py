from bs4 import BeautifulSoup
import urllib

def get_summaries():
    """Returns each summary in dictionary with the values in keys"""
    r = urllib.urlopen('http://www.govtrack.us/congress/bills/114/s1864/summary')
    soup = BeautifulSoup(r, 'html.parser')

    for p in (soup.find_all('p')):
        print(p.prettify()[0:11])

get_summaries()
