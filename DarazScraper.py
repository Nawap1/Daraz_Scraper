from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

def extract_number(s):
    start = s.find('(')
    end = s.find(')', start)
    if start != -1 and end != -1:
        number_str = s[start+1:end]
        if number_str.isdigit():
            return int(number_str)
    return None

driver = webdriver.Chrome()
pages_to_parse = 20
pages=0
df_json = {
        'Product Name':[],
        'Brand':[],
        'Product Price':[],
        'Number of Rating':[],
        'Number of Reviews':[],
    }
url = 'https://www.daraz.com.np/catalog/?q=phone&_keyori=ss&from=input&spm=..search.go.'
while True:
    pages+=1
    if pages>1:
        url = f'https://www.daraz.com.np/catalog/?_keyori=ss&from=input&page={pages}&q=phone&spm=..search.go.'
    driver.get(url)
    time.sleep(5)

    html = driver.page_source

    parsed_html = BeautifulSoup(html, "html.parser")

    products = parsed_html.find_all("div", {"class" : "info--ifj7U"})

    for product in products:

        soup = BeautifulSoup(str(product),'html.parser')
        product_name = soup.find('div', {'class': 'title--wFj93'}).text.strip()
        product_price = soup.find('div', {'class': 'price--NVB62'}).text.strip()
        rating = len(soup.find_all('i',{'class':'star-icon--k88DV star-10--UQtQk'}))
        reviews = extract_number(str(soup.find('span',{'class':'rating__review--ygkUy'})))

        df_json['Product Name'].append(product_name)
        df_json['Brand'].append(product_name.split()[0].capitalize())
        df_json['Product Price'].append(product_price)
        df_json['Number of Rating'].append(rating)
        df_json['Number of Reviews'].append(reviews)
    if pages==pages_to_parse:
        break

df = pd.DataFrame(df_json)
df.to_csv('Daraz_Phone_Dataset.csv')