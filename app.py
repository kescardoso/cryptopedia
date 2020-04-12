import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# Forms
from forms import RegistrationForm, LoginForm
# Environment variables
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

# MongoDB settings
app.config["MONGO_NAME"] = 'cryptopedia'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
# Flask settings
app.config["SECRET_KEY"] = '!gMcT*jnqvez&'

mongo = PyMongo(app)


# CRUD: bind and display list of all terms in the database:
@app.route('/')
@app.route('/get_terms')
def get_terms():
    return render_template("terms.html",
                            terms=mongo.db.terms.find())


# CRUD: get form to add new term:
@app.route('/add_term')
def add_term():
    return render_template('addterm.html',
                           categories=mongo.db.categories.find())


# CRUD: add new term to the database:
@app.route('/insert_term', methods=['POST'])
def insert_term():
    terms = mongo.db.terms
    terms.insert_one(request.form.to_dict())
    return redirect(url_for('get_terms'))


# CRUD: get form to edit term:
@app.route('/edit_term/<term_id>')
def edit_term(term_id):
    the_term = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editterm.html', term=the_term,
                           categories=all_categories)


# CRUD: edit term into the database:
@app.route('/update_term/<term_id>', methods=["POST"])
def update_term(term_id):
    terms = mongo.db.terms
    terms.update({'_id': ObjectId(term_id)}, {
        'term_name': request.form.get('term_name'),
        'category_name': request.form.get('category_name'),
        'term_description': request.form.get('term_description'),
    })
    return redirect(url_for('get_terms'))


# CRUD: delete term from the database:
@app.route('/delete_term/<term_id>')
def delete_term(term_id):
    mongo.db.terms.remove({'_id': ObjectId(term_id)})
    return redirect(url_for('get_terms'))


# CRUD: bind and display list of categories from the database
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())


# CRUD: get form to edit category
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=mongo.db.categories.find_one(
                            {'_id': ObjectId(category_id)}))


# CRUD: edit category into the database
@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


# CRUD: delete categories from the databse
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


# CRUD: get form to add new category to the database
@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


# CRUD: add new Category to the database
@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


# Search Form for glossary terms
# From: https://stackoverflow.com/questions/48371016/pymongo-how-to-use-full-text-search
# And: https://stackoverflow.com/questions/49884312/mongodb-text-index-search
@app.route('/search_terms')
def search_terms(search):
    mongo.db.terms.create_index({ term_name: "text", term_description: "text" })
    results=mongo.db.terms.find({"$text": {"$search": search}})
    return render_template("terms.html",
                            terms=results)
#Seun
# @app.route('/search_terms/<search>')
# def search_terms(search):
#     results=mongo.db.terms.find({"term_name": {'$regex': search, '$options': 'i'}})
#     return render_template("terms.html",
#                             terms=results)


# About and Guide
@app.route('/about')
def about():
    return render_template("about.html")


# User Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Success! Account created for {form.username.data}.', 'badge light-green lighten-4')
        return redirect(url_for('get_terms'))
    return render_template("register.html", title='Register', form=form)


# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Success! You have been logged in.', 'badge light-green lighten-4')
            return redirect(url_for('get_terms'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'badge red lighten-4')
    return render_template("login.html", title='Login', form=form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
