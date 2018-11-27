import requests, datetime
from bs4 import BeautifulSoup as bs

search = requests.get("https://www.google.com/search?q=bitcoin+price")
soup = bs(search.text, "html.parser")
bitcoin_price = soup.find(class_ = "J7UKTe")
bp = bitcoin_price.get_text().split()
t = datetime.datetime.now()
t = str(t.time())[:-7] + " -"
print(t, "$" + bp[3])


# Run it every three minutes as PowerShell function
# function bp {while(1){py .\bitcoin_price.py; start-sleep -seconds 180}}
