from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "César"}
    posts = [
        {"author": {"username": "Paola"}, "body": "Beautiful morning in Santiago"},
        {
            "author": {"username": "Sandino"},
            "body": "Moving to California soon. Summer 2025 here we go!",
        },
        {"author": {"username": "Welling"}, "body": "Sunny day in Berlin today! Yeah!"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
