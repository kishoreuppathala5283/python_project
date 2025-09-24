from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", message="Welcome!")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form["name"]
    return f"Hello, {name}!"
