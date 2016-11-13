from bs4 import BeautifulSoup
import urllib

def get_prognosis(bill_url):
    """Returns each summary in dictionary with the values in keys"""
    r = urllib.urlopen(bill_url)
    soup = BeautifulSoup(r, 'html.parser')

    prog = soup.find("div", {"id": "prognosis-details"})
    prog = prog.find("div", {"class": "modal-body"})


    return prog.find("p").get_text()

print get_prognosis("https://www.govtrack.us/congress/bills/114/hr1634")
