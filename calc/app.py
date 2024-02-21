from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.get("/")
def index():
    """Returns a welcome message on the homepage"""
    return "Welcome to the Homepage"

@app.get("/add")
def add_operation():
    """Returns the result of add operation"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    sum = add(a, b)

    return str(sum)

@app.get("/sub")
def sub_operation():
    """Returns the result of subtract operation"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    subtract = sub(a, b)

    return str(subtract)

@app.get("/mult")
def multi_operation():
    """Returns the result of multiply operation"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    multiply = mult(a, b)

    return str(multiply)

@app.get("/div")
def div_operation():
    """Returns the result of division operation"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    divide = div(a, b)

    return str(divide)



