from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "abcd1234"

@app.route("/hello")
def index():
    flash("¿Cómo te llamas?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    name = request.form["name_input"]
    flash("Hola " + name.capitalize() + ", que bueno verte! ")
    return render_template("index.html")