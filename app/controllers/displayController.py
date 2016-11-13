import requests
import urllib
from app.models import Bill
from app.allImports import *

from flask import render_template, Markup
from bs4 import BeautifulSoup

# url = raw_input("Enter a website to extract the URL's from: ")

# r  = requests.get("http://" +url)

# data = r.text

# soup = BeautifulSoup(data)

# for link in soup.find_all('a'):
#     print(link.get('href'))

@app.route("/display/<string:link>", methods=["GET"])
def display(link):
    page = ["DDDDDDDD","DDDDDDDDDDDDDDDDDD","E#EEEEEEEEEEEEEEEEEEE"]
    return render_template('display.html', page = page )


