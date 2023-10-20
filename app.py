from functools import wraps

from flask import Flask, render_template, session, redirect, flash, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connessione a un'istanza MongoDB locale
client = MongoClient("mongodb+srv://miniello917:<password>@gigabarber.jqoknjr.mongodb.net/?retryWrites=true&w=majority")

# Specifica il database a cui connettersi se non esiste lo crea (Collezzione ???)
db = client['db-gigabarber']
userCollection = db["users"]


# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap


def login_not_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return redirect('/')
        else:
            return f(*args, **kwargs)

    return wrap


def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session['user']['role'] == "admin":
            return f(*args, **kwargs)
        else:
            flash("You need to be an admin to view this page.")
            return redirect(url_for('home'))

    return wrap


# Routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reservation/')
def reservation():
    return render_template('reservation.html')


@app.route('/registration/')
def registration():
    return render_template('registration.html')


@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
