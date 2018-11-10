import requests
from bs4 import BeautifulSoup
import pymongo
import pandas as pd
import time
from selenium import webdriver
from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
	executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
	return Browser('chrome', **executable_path, headless=False)

def scrape():

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

	# URL of page to be scraped
	cerb_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'

	# Retrieve page with the requests module
	def render_page(cerb_url):
		driver = webdriver.Chrome()
		driver.get(cerb_url)
		time.sleep(3)
		cerb_response = driver.page_source
		#driver.quit()
		return cerb_response
	
	cerb_response = render_page(cerb_url)

	cerb_soup = BeautifulSoup(cerb_response, "html.parser")
	#print(cerb_soup.prettify())

	# Retrieve hemisphere info
	cerberus = cerb_soup.find('div', class_='wide-image-wrapper')
	# Retrieve hemisphere title
	cerb_title = cerb_soup.find('h2', class_='title').text
	# Identify and return image src
	cerb_link = cerb_soup.find('div', class_='downloads').a['href']

	# URL of page to be scraped
	schia_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'

	# Retrieve page with the requests module
	def render_page(schia_url):
		driver = webdriver.Chrome()
		driver.get(schia_url)
		time.sleep(3)
		schia_response = driver.page_source
		#driver.quit()
		return schia_response
	
	schia_response = render_page(schia_url)

	schia_soup = BeautifulSoup(schia_response, "html.parser")
	#print(schia_soup.prettify())

	# Retrieve hemisphere info
	schiaparelli = schia_soup.find('div', class_='wide-image-wrapper')
	# Retrieve hemisphere title
	schia_title = schia_soup.find('h2', class_='title').text
	# Identify and return image src
	schia_link = schia_soup.find('div', class_='downloads').a['href']

	# URL of page to be scraped
	syrtis_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'

	# Retrieve page with the requests module
	def render_page(syrtis_url):
		driver = webdriver.Chrome()
		driver.get(syrtis_url)
		time.sleep(3)
		syrtis_response = driver.page_source
		#driver.quit()
		return syrtis_response
	
	syrtis_response = render_page(syrtis_url)

	syrtis_soup = BeautifulSoup(syrtis_response, "html.parser")
	#print(cerb_soup.prettify())

	# Retrieve hemisphere info
	syrtis = syrtis_soup.find('div', class_='wide-image-wrapper')
	# Retrieve hemisphere title
	syrtis_title = syrtis_soup.find('h2', class_='title').text
	# Identify and return image src
	syrtis_link = syrtis_soup.find('div', class_='downloads').a['href']

	# URL of page to be scraped
	valles_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

	# Retrieve page with the requests module
	def render_page(valles_url):
		driver = webdriver.Chrome()
		driver.get(valles_url)
		time.sleep(3)
		valles_response = driver.page_source
		#driver.quit()
		return valles_response
	
	valles_response = render_page(valles_url)

	valles_soup = BeautifulSoup(valles_response, "html.parser")
	#print(valles_soup.prettify())

	# Retrieve hemisphere info
	valles = valles_soup.find('div', class_='wide-image-wrapper')
	# Retrieve hemisphere title
	valles_title = valles_soup.find('h2', class_='title').text
	# Identify and return image src
	valles_link = valles_soup.find('div', class_='downloads').a['href']


	# Dictionary to be inserted as a MongoDB document
	mars_current = {
		'title': title,
		'date': date,
		'url': concatURL,
		'teaser': text,
		'imgTitle': img_title,
		'imgSrc': imageURL,
		'weather': mars_weather,
		'valles_title': valles_title,
		'valles_link': valles_link,
		'syrtis_title': syrtis_title,
		'syrtis_link': syrtis_link,
		'schia_title': schia_title,
		'schia_link': schia_link,
		'cerb_title': cerb_title,
		'cerb_link': cerb_link
	}
	
	return mars_current

	#collection.insert_one(mars_current)
	#collection.update_one(mars_current)


