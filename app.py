from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "abcd1234"

@app.route("/")
def index():
    flash("¡Hola! ¿Quién sos?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    name = request.form["name_input"]
    flash("Hola " + name.capitalize() + ", no molestes por favor! Besi!")
    if len(name) > 10:
        render_template("nomol.html")
    return render_template("index.html")

@app.route("/nomol")
def nomol():
    return render_template("nomol.html")
