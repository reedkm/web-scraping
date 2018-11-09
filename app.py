from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_scraping"
mongo = PyMongo(app)


@app.route("/")
def index():
    current = mongo.db.mars_current.find_one()
    return render_template("index.html", current=current)

@app.route("/scrape")
def scraper():
    current = mongo.db.listings

    current_data = mars_scraping.scrape()
    
    current.update({}, current_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)


