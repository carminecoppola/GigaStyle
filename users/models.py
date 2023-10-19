import uuid

from flask import jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256

from app import db


class User:

    # start_session(): avvia una sessione utente. Rimuove la password dall'oggetto utente e imposta
    # una variabile di sessione per indicare che l'utente è autenticato. Quindi reindirizza l'utente
    # alla pagina /User/ e restituisce i dettagli dell'utente in formato JSON.
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        redirect('/User/')
        return jsonify(user), 200

    # signup(): gestisce la registrazione degli utenti. Raccoglie i dati dal modulo di registrazione,
    # crea un documento utente con un _id generato casualmente e fa l'hash della password dell'utente.
    # Verifica se l'email è già registrata nel database e se non lo è, salva il nuovo utente nel database,
    # avviando una sessione utente.
    def signup(self):

        user = {
            "_id": uuid.uuid4().hex,
            "first_name": request.form.get('first_name'),
            "last_name": request.form.get('last_name'),
            "phone": request.form.get('phone'),
            "email": request.form.get('email'),
            "gender": request.form.get('gender'),
            "password": request.form.get('password'),
            "role": "user"
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Email check
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email already present"}), 400
        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400

    # signout(): gestisce la disconnessione dell'utente
    def signout(self):
        session.clear()
        return redirect('/')

    # login():  gestisce il processo di login. Ricerca un utente nel database in base all'email
    # fornita e verifica la password usando l'hash. Se l'utente esiste e la password è corretta,
    # avvia una sessione utente.
    def login(self):

        user = db.users.find_one({
            "email": request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)
        else:
            return jsonify({"error": "Invalid login credentials"}), 401
