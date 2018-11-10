from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scraping

app = Flask(__name__)

# Create connection variable
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    articles =list(mongo.db.mars_current.find_one())
    print(articles)

    # Return the template with the articles list passed in
    return render_template('index.html', articles=articles)

@app.route("/scrape")
def scraper():
    current = mongo.db.mars_current

    current_data = mars_scraping.scrape()
    
    current.update({}, current_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

