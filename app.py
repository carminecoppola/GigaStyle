import secrets

from flask import Flask, request, render_template, redirect, url_for, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

uri = "mongodb+srv://miniello:pericle@cluster0.1lorjnu.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['utenti']
collection = db['utenti']
collection2 = db['booking']


# Routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/choose/')
def choose():
    return render_template('choose.html')


@app.route('/barber/', methods=['GET', 'POST'])
def barber():
    return render_template('reservationBarber.html')


@app.route('/hairdresser/', methods=['GET', 'POST'])
def hairdresser():
    return render_template('reservationHairDresser.html')


@app.route('/employees/')
def employees():
    return render_template('employees.html')


@app.route('/admin/')
def admin():
    return render_template('admin.html')


@app.route('/registrazione', methods=['GET', 'POST'])
def registrazione():
    if request.method == 'POST':
        # Ottieni i dati del modulo di registrazione
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        gender = request.form['gender']

        # Verifica se l'utente esiste già
        if collection.find_one({'email': email}):
            return 'Questa email esiste già. Scegli un altra email.'

        # Inserisci l'utente nel database con tutti i campi
        new_user = {
            'email': email,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'gender': gender
        }
        collection.insert_one(new_user)

        # Reindirizza l'utente alla pagina "choose.html" dopo la registrazione
        return redirect(url_for('choose'))

    return render_template('registration.html')


# Pagina di login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = collection.find_one({'email': email, 'password': password})

        if user:
            # Login riuscito, creiamo una sessione
            session['email'] = email

            if email == 'admin@admin.com':
                return redirect(url_for('admin'))
            elif email == 'emp@employments.com':
                return redirect(url_for('employees'))
            else:
                # Reindirizza l'utente alla pagina "choose.html" e passa l'informazione dell'email come variabile
                return redirect(url_for('choose', email=email))

        else:
            return 'Credenziali errate. Riprova o <a href="/registrazione">registrati</a>.'

    return render_template('login.html')


@app.route('success')
def success():
    return render_template('success.html')


@app.route('/logout')
def logout():
    session.pop('email', None)
    return 'Sei stato disconnesso. <a href="/">Torna alla pagina principale</a>'







if __name__ == '__main__':
    app.run()



