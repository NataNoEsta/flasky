from flask import Flask, render_template, request, flash
from random import randint

#instanciacion de la clase Flask
app = Flask(__name__)
app.secret_key = "abcd1234"


if __name__ == '__main__':
    #llamada al método run() en modo debug de la clase Flask
    app.run(debug=True)

#ruta del index.html
@app.route("/")
def index():
    flash("¡Hola! ¿Quién sos?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    name = request.form["name_input"]
    flash("Hola " + name.capitalize() + saludos())
    return render_template("byebestie.html")

def saludos():
    var_saludos = [" no molestes plis!", " vete a la m1erda uwu", " cómo estás?", " quién sos?", " un gusto, besi!"]
    limit = len(var_saludos)
    #selecciona un índice al azar y devlueve el saludo correspondiente
    x = randint(0, limit-1)
    return var_saludos[x]
