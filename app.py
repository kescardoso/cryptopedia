import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# Environment Variables
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_NAME"] = 'cryptopedia'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')


mongo = PyMongo(app)


# Main Page: List of all terms:
@app.route('/')
@app.route('/get_terms')
def get_terms():
    return render_template("terms.html",
                            terms=mongo.db.terms.find())


# CRUD: Add new term:
@app.route('/add_term')
def add_term():
    return render_template('addterm.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_term', methods=['POST'])
def insert_term():
    terms = mongo.db.terms
    terms.insert_one(request.form.to_dict())
    return redirect(url_for('get_terms'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
