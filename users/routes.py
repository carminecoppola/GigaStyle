from app import app
from users.models import User


@app.route('/user/registration', methods=['GET ,POST'])
def signup():
    return User().signup()


@app.route('/user/signout')
def signout():
    return User().signout()


@app.route('/user/login', methods=['GET,POST'])
def login2():
    return User().login()
