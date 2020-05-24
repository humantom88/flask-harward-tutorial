import csv
from flask import Flask, render_template, request

app = Flask(__name__)

FROM_EMAIL = "whatever@gmail.com"

@app.route("/")
def index():
    name = request.args.get("name", "world")
    return render_template("index.html", name=name)

@app.route("/registered")
def registered():
    with open("registered.csv", "r") as file:
        reader = csv.reader(file)
        students = list(reader)
    return render_template("registered.html", students=students)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return render_template("failure.html")
    with open("registered.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow((name, dorm))
        file.close()
    return render_template("success.html")