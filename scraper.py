from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome()

browser.get(START_URL)

scraped_data = []
stars_data=[]

time.sleep(10)

def scrape():

    
    for i in range(0,len(scraped_data)):

        Star_names = scraped_data[i][1]
        Distance = scraped_data[i][3]
        Mass = scraped_data[i][5]
        Radius = scraped_data[i][6]
        Lum = scraped_data[i][7]

        required_data = [Star_names,Distance,Mass,Radius,Lum]
        stars_data.append(required_data)

        print(f'Scraping page {i+1} ...')

        bright_star_table = soup.find("table", attrs={"class","wikitable"})

        table_body = bright_star_table.find('tbody')

        table_rows = table_body.find_all('tr')

        for row in table_rows:
             table_cols = row.find_all('td')
             temp_list = []

             for col_data in table_cols:
                 
                data = col_data.text.strip()
                temp_list.append(data)

             scraped_data.append(temp_list)

scrape()

headers = ["Star_name", 'Distance', 'Mass', 'Radius', 'Luminosity']

stars_df_1 = pd.DataFrame(stars_data,columns=headers)

stars_df_1.to_csv('scraped_data.csv',index = True,index_label="id")