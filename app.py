from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

# Set route
@app.route('/')
def index():
    # Store the articles in a list
    articles = list(db.mars_current.find())
    print(articles)

    # Return the template with the articles list passed in
    return render_template('index.html', articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
