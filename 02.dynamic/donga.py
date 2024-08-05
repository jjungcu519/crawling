import requests
from pprint import pprint
from bs4 import BeautifulSoup
URL = 'https://www.donga.com/'

res = requests.get(URL)

soup = BeautifulSoup(res.text, 'html.parser')