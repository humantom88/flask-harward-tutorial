import os
import smtplib
from flask import Flask, render_template, request

app = Flask(__name__)

FROM_EMAIL = "whatever@gmail.com"

@app.route("/")
def index():
    name = request.args.get("name", "world")
    return render_template("index.html", name=name)

@app.route("/registered")
def registrants():
    return render_template("registered.html", students=["John Doe", "Alice Cooper"])


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return render_template("failure.html")
    message = "You are registered!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(FROM_EMAIL, os.getenv("PASSWORD"))
    server.sendmail(FROM_EMAIL, email, message)

    return render_template("success_html")