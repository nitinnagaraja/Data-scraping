from pprint import pprint
import pickle
import json
import requests
from BeautifulSoup import BeautifulSoup

base_url = "http://www.iihs.org/iihs/ratings/v/class-summary/"

types = ["microcars", "minicars", "small-cars","midsize-moderately-priced-cars",
         "midsize-luxury-near-luxury-cars", "midsize-convertibles",
         "large-family-cars", "large-luxury-cars", "small-suvs", "midsize-suvs",
         "midsize-luxury-suvs", "large-suvs", "minivans", "small-pickups",
         "large-pickups"]

for t in types[:1]:
    print base_url + t
    response = requests.get(base_url + t)
    html = response.content
    soup = BeautifulSoup(html)

    #print soup
    ss = soup.findAll('div')
    #print ss
