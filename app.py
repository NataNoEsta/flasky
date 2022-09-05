from flask import Flask, render_template, request, flash
from random import randint

app = Flask(__name__)
app.secret_key = "abcd1234"

if __name__ == '__main__':
    app.run(debug=True)

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
    x = randint(0, limit-1)
    return var_saludos[x]
