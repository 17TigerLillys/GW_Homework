from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars
app = Flask(__name__)

conn="mongodb://localhost:27017"
client=pymongo.MongoClient(conn)
db =  client.mars
#mars = db.mars
mars = mongo.db.mars


@app.route("/")
def home():
	print("getting data on Mars now!!")
	new_planet = mars.find_one()
	return render_template("index.html", mars=new_planet)

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape()
    #update with upsert=True means that it will either add something new or update
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    print("finished sraping!! We're ready to redirect")
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)