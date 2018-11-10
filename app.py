from flask import Flask, render_template, redirect

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import flask_pymongo
import mars_scraping

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017/mars_db'

# Pass connection to the pymongo instance.
client = flask_pymongo.PyMongo(app, uri=conn)

# Connect to a database. Will create one if not already available.
db = client

# Set route
@app.route('/')
def index():
    # Store the articles in a list
    articles2 = list(db.db.mars_db.mars_current.find())
    #print(articles)

    # Return the template with the articles list passed in
    return render_template('index.html', articles=articles2)
    
@app.route("/scrape")
def scraper():
    current = db

    current_data = mars_scraping.scrape()
    
    current.db.mars_current.update({}, current_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
