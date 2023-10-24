from app import app
from users.models import User


@app.route('/user/signup', methods=['POST'])
def signup():
    print('Ciao ebrei luridi')
    return User().signup()


@app.route('/user/signout')
def signout():
    return User().signout()


@app.route('/user/login', methods=['POST'])
def login2():
    return User().login()
