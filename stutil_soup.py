#import request module and BS$ module
import requests
from bs4 import BeautifulSoup
r=requests.get("https://en.wikipedia.org/wiki/Computer")
print(r.text)
soup=BeautifulSoup(r.text,"html.parser")
