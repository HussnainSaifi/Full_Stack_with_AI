#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
 
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
quotes=[]  # a list to store quotes
 
table = soup.find('div', attrs = {'id':'all_items'}) 
 
for row in table.find_all('div', attrs={'class':'text-center mb-8'}):
    quote = {}
    
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    
    # alt text se sirf quote lena
    alt_text = row.img.get('alt', '')
    
    # lines (quote) clean karna
    quote['lines'] = alt_text.split(" #")[0]
    
    # author directly <p> se lena
    author_tag = row.find('p', class_='text-white/50')
    quote['author'] = author_tag.text if author_tag else "Unknown"
    
    quotes.append(quote)
 
filename = 'Week6/inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)