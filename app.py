from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reservation')
def reservation():
    return render_template('reservation.html')


if __name__ == '__main__':
    app.run()
