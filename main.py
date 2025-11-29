from flask import Flask, redirect, request
from datetime import datetime

app = Flask(__name__)

# Главная страница - делает редирект на /addition
@app.route("/")
def index():
    return redirect("/addition")

# Эндпоинт "+"
@app.route("/addition")
def addition():
    x = request.args.get("x", type=float)
    y = request.args.get("y", type=float)

    if x is None or y is None:
        return "Не переданы числа в параметрах запроса `x` и `y`"
    
    result = x + y
    return str(result)

# Эндпоинт "-"
@app.route("/subtraction")
def subtraction():
    x = request.args.get("x", type=float)
    y = request.args.get("y", type=float)

    if x is None or y is None:
        return "Не переданы числа в параметрах запроса `x` и `y`"
    
    result = x - y
    return str(result)

# Эндпоинт "*"
@app.route("/multiplication")
def multiplication():
    x = request.args.get("x", type=float)
    y = request.args.get("y", type=float)

    if x is None or y is None:
        return "Не переданы числа в параметрах запроса `x` и `y`"
    
    result = x * y
    return str(result)

# Эндпоинт "/"
@app.route("/division")
def division():
    x = request.args.get("x", type=float)
    y = request.args.get("y", type=float)

    if x is None or y is None:
        return "Не переданы числа в параметрах запроса `x` и `y`"
    if y == 0:
        return "division by zero"
    
    result = x / y
    return str(result)

if __name__ == "__main__":
    from waitress import serve
    serve(app, port=8080)
