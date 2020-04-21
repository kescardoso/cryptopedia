import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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
@app.route('/')
@app.route('/get_terms')
def get_terms():
    """ CRUD: bind and display a list of all terms in the database """
    return render_template('terms.html',
                            terms=mongo.db.terms.find().sort('term_name'))


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
                           categories=mongo.db.categories.find().sort('category_name'))


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


### CHECK THIS FOR ACCESS RESTRICTION
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    """ CRUD: delete categories from the databse """
    if 'username' in session:
        user = mongo.db.users.find_one({'user_name': session["username"]})
        if user.privilage == 'admin':
            mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


### FILTER CATEGORY BY QUERIES
@app.route('/filter_terms/<category>')
def filter_terms(category):
    """ Query Terms by Category """
    return render_template('filterterms.html',
                            terms=mongo.db.terms.find({'category_name' : category}))


### USER FORMS ROUTES
# Code credits:
# Pretty Printed Login System https://youtu.be/vVx1737auSE 
# Pretty Printed Bad request in Flask https://youtu.be/lLc_jHkifRc
# Tech Monger https://techmonger.github.io/4/secure-passwords-werkzeug/

# Register Form Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Check if username already exists, to avoid duplicates """
    if request.method == 'POST':
        existing_user = mongo.db.users.find_one({'user_name': request.form.get('username')})

        """ If username doesn't exist, create new instance for user """
        if existing_user is None:
            pwhash = generate_password_hash(request.form.get('password'))
            # hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())

            mongo.db.users.insert({ 'user_name': request.form.get('username'),
                                    'user_email': request.form.get('email'),
                                    'user_pass' : pwhash })
            session['user_name'] = request.form.get('username')
            flash('Account created successfuly. Please, log in.', 'badge light-green lighten-4')
            return redirect(url_for('login'))

        else:
            flash('Sorry! This username is already taken. If it is you, please log in.', 'badge red lighten-4')

    return render_template("register.html")


# Login Form Route
# Can't see if statements with username
@app.route("/login", methods=['GET', 'POST'])
def login():
    """ Check if username exists """
    login_user = mongo.db.users.find_one({'user_name': request.form.get('username')})

    """ If username exists, log user in """
    if login_user:
        if check_password_hash(login_user['user_pass'], request.form.get('password')):
            session['user_name'] = request.form.get('username')
            flash('Success! You have been logged in.', 'badge light-green lighten-4')
            return redirect(url_for('get_terms'))
    
        else:
            flash('Login Unsuccessful. Please check username and password.', 'badge red lighten-4')
    
    return render_template('login.html')


# Logout Form Route
# Can't see if it works and don't know how to log out
@app.route('/logout')
def logout():
    session.pop('user_name')
    flash('You were logged out.', 'badge light-green lighten-4')
    return redirect(url_for('get_terms'))


### RESTRICT ACCESS ROUTE
@app.route('/restrict')
def restrict():
    return render_template('restrict.html')


### SEARCH FORM
# From: https://stackoverflow.com/questions/48371016/pymongo-how-to-use-full-text-search
# And: https://stackoverflow.com/questions/49884312/mongodb-text-index-search
# Elasticsearch: https://dev.to/aligoren/using-elasticsearch-with-python-and-flask-2i0e
# Elasticsearch: https://medium.com/@xoor/indexing-mongodb-with-elasticsearch-2c428b676343
# ElasticSearch: https://elasticsearch-py.readthedocs.io/en/master/
# Pymongo and ES: https://github.com/ruanbekker/flask-reminders
# Pymongo ES: https://github.com/ItsRanveer/flask-mongo-elastic-REST
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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)