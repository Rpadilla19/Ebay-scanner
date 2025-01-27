import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import os


key = input("What do you want to look for? \n").replace(" ","+")

searchterm = key

def get_data(searchterm):
    url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2499334.m570.l1311&_nkw={searchterm}&_sacat=0"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse(soup):
    productslist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
            products = {
                 'title': item.find('div', {'class': 's-item__title'}).text,
                 'price': item.find('span', {'class': 's-item__price'}).text.replace('$','').strip(),
                 'link': item.find('a', {'class' : 's-item__link'})['href'],
            }
            productslist.append(products)
    return productslist

def output(productslist, searchterm):

     targetdir = "/home/bobby/scripts/pc_parts_WS/Ebay_output"
     output_path = os.path.join(targetdir, searchterm + '.csv')

     productsdf.to_csv(output_path, index=False)
     print('Ebay scraped')
     return
