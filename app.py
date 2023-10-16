from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connessione a un'istanza MongoDB locale
client = MongoClient("mongodb://localhost:27017")

# Specifica il database a cui connettersi se non esiste lo crea (Collezzione ???)
db = client['db-gigabarber']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reservation/')
def reservation():
    return render_template('reservation.html')

@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
