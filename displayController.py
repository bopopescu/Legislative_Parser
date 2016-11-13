import requests
from bs4 import BeautifulSoup

# url = raw_input("Enter a website to extract the URL's from: ")

# r  = requests.get("http://" +url)

# data = r.text

# soup = BeautifulSoup(data)

# for link in soup.find_all('a'):
#     print(link.get('href'))

@app.route("/display/<link>", methods=["GET"])
def display(link):
    print("JHEEL")
    request = requests.get(link) 
    page = BeautifulSoup(request)
    div = page.find_all("div", { "class" : "col-sm-8 col-sm-pull-4" })
    print("HELEL")
    return render_template('display.html', page = page )


