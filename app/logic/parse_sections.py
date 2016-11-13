from bs4 import BeautifulSoup
import urllib

def get_sections(bill_url):
    """Returns each summary in dictionary with the values in keys"""
    r = urllib.urlopen(bill_url)
    soup = BeautifulSoup(r, 'html.parser')

    bill = soup.find("div", {"id": "main_text_content"})
    data = {}

    for section in bill.find_all('section'):
        try:
            id = int(section.get("data-citation-path"))
            data[id] = section.get_text()
        except:
            pass

    return data

#get_sections('http://www.govtrack.us/congress/bills/114/s1864/text')
