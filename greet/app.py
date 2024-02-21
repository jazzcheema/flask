from flask import Flask, request

app = Flask(__name__)

# index home page


@app.get('/')
def index():
    return 'Hello, Homepage'


@app.get('/welcome')
def welcome():
    return "welcome"


@app.get('/welcome/home')
def welcome_home():
    return "welcome home"


@app.get('/welcome/back')
def welcome_back():
    return "welcome back"
