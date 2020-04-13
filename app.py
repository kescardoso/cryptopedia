import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt
# Forms
from forms import *
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
# Flask login app:
app.config['SECRET_KEY'] = '!gMcT*jnqvez&'
login_manager = LoginManager()
login_manager.init_app(app)
# Bcrypt app:
bcrypt = Bcrypt(app)


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


### USER CLASSES
# Code credits:
# SatackOverflow: https://stackoverflow.com/questions/54992412/flask-login-usermixin-class-with-a-mongodb
# Corey Schafer: https://youtu.be/UIJKdCIEXUQ
class User:
    def __init__(self, username):
        self.username = username
        self.email = Email
        self.password = passoword

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def check_password(password_hash, password):
        return check_password_hash(password_hash, password)


### FLASK-LOGIN MANAGER ROUTE
# Code credits:
# Flask-Login Read the Docs: https://flask-login.readthedocs.io/en/latest/
# User Loader Callback
@login_manager.user_loader
def load_user(username):
    """ Reloads the user object from the user ID stored in the session """
    u = mongo.db.users.find_one(_id)
    if not u:
        return None
    return user(username=u['user_name'])


### USER FORMS ROUTES
# Code credits:
# SatackOverflow: https://stackoverflow.com/questions/54992412/flask-login-usermixin-class-with-a-mongodb
# Pretty Printed: https://youtu.be/vVx1737auSE
# Register User 
@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Register new user to the db via form with validators and alerts """
    form = RegistrationForm()
    if form.validate_on_submit():

        if request.method == 'POST':
            """ Check if username already exists, to avoid duplicates """
            existing_user = mongo.db.users.find_one({'user_name': form.username.data})

            flash('Sorry! This username is already taken. If it is you, please log in.', 'badge red lighten-4')
            return render_template("register.html", title='Register', form=form)

        """ If username doesn't exist, create new instance of user """
        if existing_user is None:
            password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            mongo.db.users.insert({ 'user_name': form.username.data,
                                    'user_email': form.email.data,
                                    'user_pass' : password_hash })
            session['username'] = form.username.data
            flash(f'Success! Account created for {form.username.data}. Please, log in.', 'badge light-green lighten-4')
            return redirect(url_for('login'))

    return render_template("register.html", title='Register', form=form)


# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    """ User login form with validators and alerts """
    if current_user.is_authenticated:
        return redirect(url_for('get_terms'))
    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.users.find_one({"user_name": form.username.data})

        if form.username.data == 'adminblog' and form.password.data == 'password':
            flash(f'Success! You have been logged in as {form.username.data}.', 'badge light-green lighten-4')
            return redirect(url_for('get_terms'))
            
        else:
            flash('Login Unsuccessful. Please check username and password.', 'badge red lighten-4')
    return render_template("login.html", title='Login', form=form)


### SEARCH FORM
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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
