import requests, datetime
from bs4 import BeautifulSoup as bs

#Yahoo Finance Version
search = requests.get("https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD")
soup = bs(search.text, "html.parser")
bitcoin_price = soup.find("span", class_ = "Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)")
try:
    bp = bitcoin_price.get_text().split()
    t = datetime.datetime.now()
    t = str(t.time())[:-7] + " -"
    print(t, "$" + bp[0])
except:
    pass


# Google Version
search = requests.get("https://www.google.com/search?q=bitcoin+price")
soup = bs(search.text, "html.parser")
bitcoin_price = soup.find(class_ = "J7UKTe")
try:
    bp = bitcoin_price.get_text().split()
    t = datetime.datetime.now()
    t = str(t.time())[:-7] + " -"
    print(t, "$" + bp[3])
except:
    pass


# Run it every three minutes as PowerShell function
# function bp {while(1){py .\bitcoin_price.py; start-sleep -seconds 180}}
