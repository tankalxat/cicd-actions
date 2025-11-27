from flask import Flask, redirect, request
from datetime import datetime

app = Flask(__name__)

# Главная страница - перенаправляет на /readme
@app.route("/")
def index():
    return redirect("/attidion")

# Эндпоинт "+"
@app.route("/attidion")
def attidion():
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
    
    result = x / y
    return str(result)

if __name__ == "__main__":
    # Запускаем сервер на порту 5000
    # app.run(host="0.0.0.0", port=5000)
    from waitress import serve
    serve(app, port=80)
