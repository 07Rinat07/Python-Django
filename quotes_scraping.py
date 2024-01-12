# http://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup

response = requests.get('http://quotes.toscrape.com/')

print(response.text)