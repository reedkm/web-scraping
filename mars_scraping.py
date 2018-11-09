import requests
from bs4 import BeautifulSoup
import pymongo
import pandas as pd
import time
from selenium import webdriver

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.mars_db
collection = db.mars_current

# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'
# Base URL for make relative links explicit
base_url = 'https://mars.nasa.gov'

# Retrieve page with the requests module
def render_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    response = driver.page_source
    #driver.quit()
    return response
    
response = render_page(url)

soup = BeautifulSoup(response, "html.parser")
#print(soup.prettify())

# Retrieve latest news article
news = soup.find('li', class_='slide')

title = news.find('div', class_='content_title').text
# Identify and return title
date = news.find('div', class_='list_date').text
# Identify and return link
link = news.a['href']
# Identify and return teaser text
text = news.find('div', class_='article_teaser_body').text
   
# Concat URL
concatURL = base_url + link

# URL of page to be scraped
image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
# Base URL for make relative links explicit
image_base_url = 'https://www.jpl.nasa.gov'

# Retrieve page with the requests module
def render_page(image_url):
    driver = webdriver.Chrome()
    driver.get(image_url)
    time.sleep(3)
    image_response = driver.page_source
    #driver.quit()
    return image_response
    
image_response = render_page(image_url)

image_soup = BeautifulSoup(image_response, "html.parser")
#print(image_soup.prettify())

# Retrieve image result
image_results = image_soup.find('footer')

# Identify and return image title
img_title = image_results.a['data-title']
# Identify and return image src
img_link = image_results.a['data-fancybox-href']
     
# Concat URL
imageURL = image_base_url + img_link



# URL of page to be scraped
weather_url = 'https://twitter.com/marswxreport?lang=en'

# Retrieve page with the requests module
def render_page(weather_url):
    driver = webdriver.Chrome()
    driver.get(weather_url)
    time.sleep(3)
    weather_response = driver.page_source
    #driver.quit()
    return weather_response

weather_response = render_page(weather_url)

weathersoup = BeautifulSoup(weather_response, "html.parser")
#print(weathersoup.prettify())

# Get Current Weather
weather = weathersoup.find('div', class_='js-tweet-text-container')

mars_weather = weathersoup.find('p', class_='tweet-text').text

# URL of page to be scraped
facts_url = 'http://space-facts.com/mars/'

# Retrieve page with the requests module
def render_page(facts_url):
    driver = webdriver.Chrome()
    driver.get(facts_url)
    time.sleep(3)
    facts_response = driver.page_source
    #driver.quit()
    return facts_response
    
facts_response = render_page(facts_url)

facts_soup = BeautifulSoup(facts_response, "html.parser")
#print(facts_soup.prettify())

tables = pd.read_html(facts_url)
tables

table_df = tables[0]
table_df.columns = ['Description', 'Value']
table_df.reset_index(drop = True)

table_df.to_html('table.html')

# Dictionary to be inserted as a MongoDB document
mars_current = {
    'title': title,
    'date': date,
    'url': concatURL,
    'teaser': text,
    'imgTitle': img_title,
    'imgSrc': imageURL,
    'weather': mars_weather
}

collection.insert_one(mars_current)


