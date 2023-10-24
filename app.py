from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

uri = "mongodb+srv://miniello:pericle@cluster0.1lorjnu.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.DBUtenti
coll = db.utenti


# Routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    print('Africani bastardi')
    return render_template('registration.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    print('Luridi Africani bastardi')
    return render_template('login.html')


@app.route('/reservation/')
def reservation():
    return render_template('reservationBarber.html')


@app.route('/choose/')
def choose():
    print('Choose fratm ennar')
    return render_template('choose.html')


@app.route('/barber/')
def barber():
    return render_template('reservationBarber.html')


@app.route('/hairdresser/')
def hairdresser():
    return render_template('reservationHairDresser.html')


if __name__ == '__main__':
    app.run()
