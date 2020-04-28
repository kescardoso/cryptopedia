import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_paginate import Pagination, get_page_args
# Environment variables
from os import path
if path.exists('env.py'):
    import env


# Flask app:
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
# MongoDB settings:
app.config['MONGO_NAME'] = 'cryptopedia'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
# Pymongo app:
mongo = PyMongo(app)


### CRUD ROUTES

# Glossary and Search
# Code credits:
# DarilliGames Flask Paginate https://github.com/DarilliGames/flaskpaginate

# Pagination function
""" Glossary of terms with pagination """
def paginated_terms(offset=0, per_page=10):
    terms = mongo.db.terms.find().sort('term_name')
    print("herl")
    return terms[offset: offset + per_page]

# Display glossary of terms
@app.route('/')
@app.route('/glossary')
def glossary():
    """ Pagination for glossary """
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    """ CRUD: bind and display a list of all terms in the db as a glossary with pagination """
    total = mongo.db.terms.find().sort('term_name').count()
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materialize')
    paginatedTerms = paginated_terms(offset=offset, per_page=per_page)
    return render_template('terms.html',
                            terms=paginatedTerms,
                            page=page,
                            per_page=per_page,
                            pagination=pagination,
                            )

# Full text Search
@app.route('/search_terms', methods=['POST'])
def search_terms():
    search = request.form.get('search')
    print(search)
    """ Pagination for search """
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    mongo.db.terms.create_index([ ('term_name', 'text'), ('term_description', 'text') ])
    results = mongo.db.terms.find({"$text": {"$search": search}})
    pagination = Pagination(page=page, per_page=per_page, results=results,
                            css_framework='materialize')
    paginatedTerms = paginated_terms(offset=offset, per_page=per_page)
    return render_template("terms.html",
                            terms=results,
                            page=page,
                            per_page=per_page,
                            pagination=pagination,
                            )


# Add new term
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
    return redirect(url_for('glossary'))


# Edit term
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
    return redirect(url_for('glossary'))


# Delete term
@app.route('/delete_term/<term_id>')
def delete_term(term_id):
    """ CRUD: delete term from the database """
    mongo.db.terms.remove({'_id': ObjectId(term_id)})
    return redirect(url_for('glossary'))


# Display categories
@app.route('/categories')
def categories():
    """ CRUD: bind and display list of categories from the database """
    return render_template('categories.html',
                           categories=mongo.db.categories.find().sort('category_name'))


# Add new category
@app.route('/add_category')
def add_category():
    """ CRUD: get form to add new category to the database """
    return render_template('addcategory.html')


@app.route('/insert_category', methods=['POST'])
def insert_category():
    """ CRUD: add new Category to the database """
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('categories'))


# Edit category
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
    return redirect(url_for('categories'))


# Delete category
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    """ CRUD: delete categories from the databse """
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('categories'))


### FILTER TERMS BY CATEGORY QUERIES
@app.route('/terms_in/<category>')
def terms_in(category):
    """ Query Terms by Category """
    return render_template('filterterms.html', category=category,
                            terms=mongo.db.terms.find({'category_name' : category}).sort('term_name'))


### CREDITS ROUTE
@app.route('/credits')
def credits():
    return render_template('credits.html')


### USER FORMS ROUTES
# Code credits:
# Pretty Printed Login System https://youtu.be/vVx1737auSE 
# Pretty Printed Bad request in Flask https://youtu.be/lLc_jHkifRc
# Tech Monger https://techmonger.github.io/4/secure-passwords-werkzeug/

# Register Form
@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Check if username already exists, to avoid duplicates """
    if request.method == 'POST':
        existing_user = mongo.db.users.find_one({'user_name': request.form.get('username')})
        """ If username doesn't exist, create new instance for user """
        if existing_user is None:
            pwhash = generate_password_hash(request.form.get('password'))
            mongo.db.users.insert({ 'user_name': request.form.get('username'),
                                    'user_email': request.form.get('email'),
                                    'user_pass' : pwhash })
            session['user_name'] = request.form.get('username')
            flash('Account created successfuly. Please, log in.', 'badge light-green lighten-4')
            return redirect(url_for('login'))
        else:
            flash('Sorry! This username is already taken. If it is you, please log in.', 'badge red lighten-4')
    return render_template("register.html")


# Login Form
@app.route("/login", methods=['GET', 'POST'])
def login():
    """ Check if username exists """
    login_user = mongo.db.users.find_one({'user_name': request.form.get('username')})
    """ If username exists, log user in """
    if login_user:
        if check_password_hash(login_user['user_pass'], request.form.get('password')):
            session['user_name'] = request.form.get('username')
            flash('Success! You have been logged in.', 'badge light-green lighten-4')
            return redirect(url_for('glossary'))    
        else:
            flash('Login Unsuccessful. Please check username and password.', 'badge red lighten-4')    
    return render_template('login.html')


# Logout
@app.route('/logout')
def logout():
    session.pop('user_name')
    flash('You were logged out.', 'badge light-green lighten-4')
    return redirect(url_for('glossary'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
