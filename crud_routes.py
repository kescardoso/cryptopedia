import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# Environment variables
from os import path
if path.exists('env.py'):
    import env


# Flask app:
app = Flask(__name__)
# MongoDB settings:
app.config['MONGO_NAME'] = 'cryptopedia'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
# Pymongo app:
mongo = PyMongo(app)


### CRUD ROUTES
@app.route('/')
@app.route('/get_terms')
def get_terms():
    """ CRUD: bind and display a list of all terms in the database """
    return render_template('terms.html',
                            terms=mongo.db.terms.find())


@app.route('/add_term')
def add_term():
    """ CRUD: get form to add new term """
    return render_template('addterm.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_term', methods=['POST'])
def insert_term():
    """ CRUD: add new term to the database """
    terms = mongo.db.terms
    terms.insert_one(request.form.to_dict())
    return redirect(url_for('get_terms'))


@app.route('/edit_term/<term_id>')
def edit_term(term_id):
    """ CRUD: get form to edit term """
    the_term = mongo.db.terms.find_one({'_id': ObjectId(term_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editterm.html', term=the_term,
                           categories=all_categories)


@app.route('/update_term/<term_id>', methods=['POST'])
def update_term(term_id):
    """ CRUD: edit term into the database """
    terms = mongo.db.terms
    terms.update({'_id': ObjectId(term_id)}, {
        'term_name': request.form.get('term_name'),
        'category_name': request.form.get('category_name'),
        'term_description': request.form.get('term_description'),
    })
    return redirect(url_for('get_terms'))


@app.route('/delete_term/<term_id>')
def delete_term(term_id):
    """ CRUD: delete term from the database """
    mongo.db.terms.remove({'_id': ObjectId(term_id)})
    return redirect(url_for('get_terms'))


@app.route('/get_categories')
def get_categories():
    """ CRUD: bind and display list of categories from the database """
    return render_template('categories.html',
                           categories=mongo.db.categories.find())


@app.route('/add_category')
def add_category():
    """ CRUD: get form to add new category to the database """
    return render_template('addcategory.html')


@app.route('/insert_category', methods=['POST'])
def insert_category():
    """ CRUD: add new Category to the database """
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    """ CRUD: get form to edit category """
    return render_template('editcategory.html',
                           category=mongo.db.categories.find_one(
                            {'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    """ CRUD: edit category into the database """
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))

 
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    """ CRUD: delete categories from the databse """
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


### ABOUT / GUIDE ROUTE
@app.route('/about')
def about():
    return render_template("about.html")
    