from functools import wraps

from flask import Flask, render_template, session, redirect, flash, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connessione a un'istanza MongoDB locale
client = MongoClient("mongodb+srv://miniello917:<supermino>@gigabarber.jqoknjr.mongodb.net/")

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
            return redirect(url_for('choose'))

    return wrap


# Routes

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration/')
@login_not_required
def registration():
    return render_template('registration.html')


@app.route('/login/')
@login_not_required
def login():
    return render_template('login.html')


@app.route('/reservation/')
@login_required
def reservation():
    return render_template('reservationBarber.html')


@app.route('/choose/')
@login_required
def choose():
    return render_template('choose.html')


@app.route('/barber/')
@login_required
def barber():
    return render_template('reservationBarber.html')


@app.route('/hairdresser/')
@login_required
def hairdresser():
    return render_template('reservationHairDresser.html')


if __name__ == '__main__':
    app.run()
