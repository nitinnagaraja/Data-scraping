from pprint import pprint
import pickle
import json
import requests
from BeautifulSoup import BeautifulSoup

base_url = "http://www.edmunds.com"
new_cars = base_url + "/new-cars/"
response = requests.get(new_cars)
html = response.content
soup = BeautifulSoup(html)

ss = soup.findAll('div', attrs = {'class': 'content grid-138'})[1]
s = ss.findAll('a')

makes = []
for item in s:
    m = str(item['href'].split('/')[1])
    makes.append(m)
    
urls = []
for m in makes:
    s = base_url + "/" + m
    urls.append(s)

l = 0

crawl_list = []
car_list = []
for test in urls[:1]:
    response = requests.get(test)
    html = response.content
    model_soup = BeautifulSoup(html)

    s = model_soup.findAll('a', attrs = {'class': 'canonicalLink'})

    for item in s:
        temp = item['href']
        
        year_response = requests.get(base_url + temp)
        year_html = year_response.content
        year_soup = BeautifulSoup(year_html)

        years =  year_soup.findAll('div', attrs = {'class': 'vehicle-card new-vm sh-none'})
        for div in years:
            st = str(div.find('div', attrs = {'class': 'info1'}).find('a')['href'])
            st += "safety/"
            car_list.append(st)

with open('nhtsa-safety-ratings2.txt', 'w+') as f:
    st = ""
    for c in car_list[:1]:
        name = '_'.join(c.split('/')[1:5])
        response = requests.get(base_url + c)
        html = response.content
        soup = BeautifulSoup(html)

        s = soup.findAll('ul', attrs = {'class': 'grid-64'})[1].findAll('li')        
        st = name

        if len(s) == 1:
            f.write(st + "\n")
            continue

        s.pop(-2)
        for item in s:
            try:
                x = item.find('div', attrs = {'class': 'rating-big'})['title']
                st = st + " " + x.split()[0]
            except:
                x = str(item.find('span', attrs = {'class': 'nhtsa-value'}).text)
                st = st + " " + x[:-1]

        f.write(st + "\n")

print "DONE!"
