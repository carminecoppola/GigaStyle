import json
import secrets

import bcrypt
from bson import json_util, ObjectId
from flask import Flask, request, render_template, redirect, url_for, session, flash
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
collection3 = db['services']


# Routes - credo che qui sia inutile il controllo sulle sessioni
@app.route('/')
def index():
    session['visited'] = True
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signUp():
    # Verifica se la richiesta è di tipo POST, ovvero se è stata inviata una form
    if request.method == 'POST':
        # Ottieni i dati del modulo di registrazione dalla form inviata
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        gender = request.form['gender']

        # Crea un hash della password prima di archiviarlo nel database per migliorare la sicurezza delle password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Verifica se l'utente esiste già nel database in base all'email fornita
        if collection.find_one({'email': email}):
            flash('Questa email esiste già. Scegli un altra email.', 'alert alert-danger')
            return redirect(url_for('signUp'))

        # Crea un nuovo utente con i dati forniti
        new_user = {
            'email': email,
            'password': hashed_password,
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'gender': gender
        }
        collection.insert_one(new_user)

        # Imposta la sessione con l'email dell'utente dopo la registrazione
        session['user'] = json.loads(json_util.dumps(new_user))

        # Reindirizza l'utente alla pagina "choose.html" dopo la registrazione
        return redirect(url_for('choose'))

    # Se la richiesta non è di tipo POST (ad esempio, una richiesta GET), visualizza la pagina di registrazione
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Verifica se la richiesta è di tipo POST, ovvero se è stata inviata una form
    if request.method == 'POST':
        # Ottieni l'email e la password dalla form inviata
        email = request.form['email']
        password = request.form['password']

        # Cerca l'utente nel database in base all'email fornita
        user = collection.find_one({'email': email})

        # Se l'utente esiste
        if user:
            session['user'] = json.loads(json_util.dumps(user))
            url = request.referrer

            # Verifica se la password fornita corrisponde all'hash della password memorizzata
            if bcrypt.hashpw(password.encode('utf-8'), user['password']) == user['password']:
                # Login riuscito, crea una sessione con l'email dell'utente
                # Se l'utente è un amministratore, reindirizzalo alla pagina "admin"
                if email == 'admin@admin.com':
                    session['visited'] = False
                    return redirect(url_for('admin'))
                # Se l'utente è un dipendente, reindirizzalo alla pagina "employees"
                elif '@employments.com' in email:
                    session['visited'] = False
                    return redirect(url_for('employees'))
                else:
                    session['visited'] = True
                    # Altrimenti, reindirizza l'utente alla pagina "choose.html" e passa l'email come variabile
                    if url.endswith('/login'):
                        return redirect(url_for('choose'))
                    elif url.endswith('/home'):
                        return redirect(url_for('homePage'))
            else:
                # Password errata, mostra un messaggio di errore
                flash('Credenziali errate', 'alert alert-danger')
                return redirect(url_for('login'))
        else:
            # L'utente non esiste, mostra un messaggio di errore
            flash('Credenziali errate', 'alert alert-danger')
            return redirect(url_for('login'))

    # Se la richiesta non è di tipo POST (ad esempio, una richiesta GET), visualizza la pagina di login
    return render_template('login.html')


@app.route('/admin')
def admin():
    if 'user' in session:
        numBarber = db.utenti.count_documents({"role": "barber"})
        numHair = db.utenti.count_documents({"role": "hairdresser"})

        return render_template('admin.html', numBarber=numBarber, numHair=numHair)
    else:
        return redirect(url_for('login'))


@app.route('/employees')
def employees():
    if 'user' in session:
        return render_template('employees.html')
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    session['visited'] = True
    return render_template('index.html')


@app.route('/choose')
def choose():
    if 'user' in session:
        return render_template('choose.html')
    else:
        return redirect(url_for('login'))


@app.route('/barber', methods=['GET', 'POST'])
def barber():
    if request.method == 'POST':
        # Ottieni i dati del modulo di prenotazione
        full_name = request.form['full_name']
        phone = request.form['phone']
        time = request.form['time']
        date = request.form['date']
        employe = request.form['chooseBarber']
        typeS = request.form['typeS']

        # Inserisci la prenotazione nel database
        new_booking = {
            'full_name': full_name,
            'phone': phone,
            'time': time,
            'date': date,
            'employe': employe,
            'typeS': typeS,
            'email': session['user']['email']
        }

        collection2.insert_one(new_booking)
        return render_template('confirmed.html')

    return render_template('reservationBarber.html')


@app.route('/hairdresser', methods=['GET', 'POST'])
def hairdresser():
    if request.method == 'POST':
        # Ottieni i dati del modulo di prenotazione
        full_name = request.form['full_name']
        phone = request.form['phone']
        time = request.form['time']
        date = request.form['date']
        employe = request.form['hdresser']
        typeS = request.form['typeS']

        # Inserisci la prenotazione nel database
        new_booking = {
            'full_name': full_name,
            'phone': phone,
            'time': time,
            'date': date,
            'employe': employe,
            'typeS': typeS,
            'email': session['user']['email']
        }

        collection2.insert_one(new_booking)
        return render_template('confirmed.html')

    return render_template('reservationHairDresser.html')


@app.route('/reservationEmployees')
def reservationEmployees():
    cursor = db.booking.find({"employe": session['user']['first_name']})
    reservation = {}

    for doc in cursor:
        reservation[str(doc['_id'])] = {
            "full_name": doc.get("full_name"),
            "time": doc.get("time"),
            "date": doc.get("date"),
            "typeS": doc.get("typeS"),
            "phone": doc.get("phone")
        }

    return render_template('reservationEmployees.html', cursor=reservation)


@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' in session:
        if '@employments.com' in session['user']['email']:
            return render_template('employees.html')
        elif session['user']['email'] == 'admin@admin.com':
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('homePage'))
    else:
        return render_template('login.html')


@app.route('/homePage')
def homePage():
    cursor = db.booking.find({"email": session['user']['email']})
    booking = {}

    for doc in cursor:
        booking[str(doc['_id'])] = {
            "email": doc.get("email"),
            "time": doc.get("time"),
            "date": doc.get("date"),
            "typeS": doc.get("typeS"),
            "employe": doc.get("employe")
        }

    return render_template('homePage.html', cursor=booking)


@app.route('/confirmed')
def confirmed():
    return render_template('confirmed.html')


@app.route('/delete/<string:booking_id>', methods=['GET'])
def delete(booking_id):
    booking_id_object = ObjectId(booking_id)
    db.booking.delete_one({"_id": booking_id_object})

    return render_template('delete.html')


@app.route('/modifyUser')
def modify():
    return render_template('modifyUser.html')


@app.route('/modifyPrice/<string:type>', methods=['GET', 'POST'])
def modifyPrice(type):
    cursor = db.services.find({"type": type})
    prices = {}
    if type == "barber":
        for doc in cursor:
            prices[str(doc['_id'])] = {
                "haircut": doc.get("haircut"),
                "beard": doc.get("beard"),
                "hbeard": doc.get("hbeard"),
                "shave": doc.get("shave"),
                "chaircut": doc.get("chaircut")
            }

        if request.method == 'POST':

            haircut = request.form['haircut']
            beard = request.form['beard']
            hbeard = request.form['hbeard']
            shave = request.form['shave']
            chaircut = request.form['chaircut']

            db.services.update_one({"type": "barber"}, {"$set": {"haircut": haircut}})
            db.services.update_one({"type": "barber"}, {"$set": {"beard": beard}})
            db.services.update_one({"type": "barber"}, {"$set": {"hbeard": hbeard}})
            db.services.update_one({"type": "barber"}, {"$set": {"shave": shave}})
            db.services.update_one({"type": "barber"}, {"$set": {"chaircut": chaircut}})
            return render_template('confirmed.html')

        return render_template('modifyPriceB.html', cursor=prices)
    elif type == "hairdresser":
        for doc in cursor:
            prices[str(doc['_id'])] = {
                "haircut": doc.get("haircut"),
                "styling": doc.get("styling"),
                "coloring": doc.get("coloring"),
                "extensions": doc.get("extensions"),
                "keratin": doc.get("keratin")
            }

        if request.method == 'POST':

            haircut = request.form['haircut']
            styling = request.form['styling']
            coloring = request.form['coloring']
            extensions = request.form['extensions']
            keratin = request.form['keratin']

            db.services.update_one({"type": "hairdresser"}, {"$set": {"haircut": haircut}})
            db.services.update_one({"type": "hairdresser"}, {"$set": {"styling": styling}})
            db.services.update_one({"type": "hairdresser"}, {"$set": {"coloring": coloring}})
            db.services.update_one({"type": "hairdresser"}, {"$set": {"extensions": extensions}})
            db.services.update_one({"type": "hairdresser"}, {"$set": {"keratin": keratin}})
            return render_template('confirmed.html')

        return render_template('modifyPriceHD.html', cursor=prices)


@app.route('/viewEmployees')
def viewEmployees():
    return render_template('viewB.html')
    # return render_template('viewHD.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
