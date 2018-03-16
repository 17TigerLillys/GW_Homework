# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser

# import necessary libraries
from flask import Flask, render_template
import pymongo
# @TODO: Initialize your Flask app here
app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.hurricane
collection = db.hurricane

#db.collection.insert_many([{"name": "hw_11", "reason": "it made absolutely no sense"}, 
#		{"name": "hw_12", "reason": "Miriam hated it, nuff said." }]
#)
@app.route("/")
def index():

	conn = 'mongodb://localhost:27017'
	client = pymongo.MongoClient(conn)
	db = client.mars
	mars = db.mars
@app.route("/scrape")

	url = 'https://mars.nasa.gov/news/'
	html = requests.get(url)
	# Create BeautifulSoup object; parse with 'html.parser'
	soup = BeautifulSoup(html.text, 'html.parser')
	results = soup.find_all('div', class_='content_title')

	mars_data=scrape_mars.scrape()

if __name__ == "__main__":
    app.run(debug=True)







