def Scrape():
	from bs4 import BeautifulSoup
	import requests
	from splinter import Browser
	#NEWS
	title = soup.find("div", "content_title", "a").contents[1].string
	paragraph = soup.find("div", "rollover_description_inner").string

	#FEATURED IMAGE
	url ="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	html = requests.get(url)
	soup = BeautifulSoup(html.text, 'html.parser')

	more_html = soup.find("div", class_="carousel_items").contents[1]
	half_of_link=more_html["style"].split("url('")
	half_of_link_clean=half_of_link[1].split("');")[0]

	featured_image_url = "https://www.jpl.nasa.gov" + half_of_link_clean

	#WEATHER
	url="https://twitter.com/marswxreport?lang=en"
	html = requests.get(url)
	soup = BeautifulSoup(html.text, 'html.parser')

	tweets=soup.find_all("p", "TweetTextSize")

	for tweet in tweets:
	    if "Sol" in tweet.text:
	        mars_weather=tweet.text
	        break

	#MARS FACTS
	url="https://space-facts.com/mars/"
	html = requests.get(url)
	soup = BeautifulSoup(html.text, 'html.parser')

	columns=soup.find_all("td", "column-1")
	column_1_list=[]
	for column in columns:
	    column_1_list.append(column.text)

	facts_columns=soup.find_all("td", "column-2") 
	column_fact_list=[]
	for fact in facts_columns:
	    column_fact_list.append(fact.text)

	mars_fact_df=pd.DataFrame({"Info Type": column_1_list, "Info": column_fact_list})

	mars_fact_df=mars_fact_df[["Info Type", "Info"]]
	mars_fact_df.set_index("Info Type", inplace=True)

	mars_fact_table = mars_fact_df.to_html(classes='table',index=False,escape=False)

	#IMAGES
	url="https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"
	html = requests.get(url)
	soup = BeautifulSoup(html.text, 'html.parser')

	executable_path = {'executable_path':'chromedriver'}
	browser = Browser('chrome', **executable_path) 
	urls_list=[]
	url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
	browser.visit(url)

	#valles marineris
	button = browser.find_link_by_partial_href("valles_marineris")
	button.click()

	current_url = browser.url
	page = requests.get(current_url)
	soup = BeautifulSoup(page.text, 'html.parser')

	image_url = soup.find(id = "wide-image").contents[3]
	title = soup.find("h2").string
	title=title.replace("Enhanced", "")

	info = {"title": title, "img_url": "https://astrogeology.usgs.gov" + image_url['src']}
	urls_list.append(info)

	browser.back()

	#cerberus
	button = browser.find_link_by_partial_href("cerberus")
	button.click()

	current_url = browser.url
	page = requests.get(current_url)
	soup = BeautifulSoup(page.text, 'html.parser')

	image_url = soup.find(id = "wide-image").contents[3]
	title = soup.find("h2").string
	title=title.replace("Enhanced", "")

	info = {"title": title, "img_url": "https://astrogeology.usgs.gov" + image_url['src']}
	urls_list.append(info)

	browser.back()

	#schiaparelli
	button = browser.find_link_by_partial_href("schiaparelli")

	button.click()

	current_url = browser.url
	page = requests.get(current_url)
	soup = BeautifulSoup(page.text, 'html.parser')

	image_url = soup.find(id = "wide-image").contents[3]
	title = soup.find("h2").string
	title=title.replace("Enhanced", "")

	info = {"title": title, "img_url": "https://astrogeology.usgs.gov" + image_url['src']}
	urls_list.append(info)

	browser.back()

	#syrtis major
	button = browser.find_link_by_partial_href("syrtis_major")
	button.click()

	current_url = browser.url
	page = requests.get(current_url)
	soup = BeautifulSoup(page.text, 'html.parser')

	image_url = soup.find(id = "wide-image").contents[3]
	title = soup.find("h2").string
	title=title.replace("Enhanced", "")

	info = {"title": title, "img_url": "https://astrogeology.usgs.gov" + image_url['src']}
	urls_list.append(info)

	browser.quit()

	mars_dict = {"news_paragraph": paragraph, "news_title": title, "weather": mars_weather, "mars_facts": mars_fact_table,
		                "featured_image": featured_image_url, "hemisphere_image_urls": urls_list}
	return mars_dict