from app import app
from flask import render_template, flash, redirect, request
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
    if login.validate_on_submit():
        flash("Successfully validated user = {} with tag {}".format(login.username.data, login.remember_me.data))
        return redirect(url_for('index'))

    return render_template("login.html", form = login, title="Login")
