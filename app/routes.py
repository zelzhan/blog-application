from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {"username":"Elzhan"}
    posts = [
        {
            'author': {'username': 'Assylzhan'},
            'body': 'Beautiful day in Kazakhstan!'
        },
        {
            'author': {'username': 'David'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='home', user=user, posts=posts)

@app.route('/login', methods=['POST', 'GET'])
def login():
    login = LoginForm()
    return render_template("login.html", form = login, title="Login")
