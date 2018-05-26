#!/usr/bin/env conda
# -*- coding: utf-8 -*-
"""
* ****************************************************************************
*      Owner: stayal0ne <elzhan.zeinulla@nu.edu.kz>                          *
*      Github: https://github.com/zelzhan                                    *
*      Created: Sat May 26 12:51:40 2018 by stayal0ne                                        *
******************************************************************************
"""

from flask import Flask, render_template
from peewee import database, SqliteDatabase, CharField, Model, ForeignKeyField, TextField, auth_user
from playhouse.flask_utils import get_object_or_404, object_list

app = Flask(__name__)

@app.before_request
def before_request():
    database.connect()

@app.after_request
def after_request(response):
    database.close()
    return response

@app.route('/')
def hello():
    return render_template('home.html')

db = SqliteDatabase('notes.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique = True)
    password = CharField()
    email = CharField(unique = True)

    def following(self):
        return (User
            .select()
            .join(Relationship, on=Relationship.to_user)
            .where(Relationship.from_user == self)
            .order_by(User.username))

    def followers(self):
        return (User
                .select()
                .join(Relatinoship, on=Relationship.from_user)
                .where(Relationship.to_user = self)
                .order_by(User.username))

try:
    with database.atomic():
        user = User.create(
            username=request.form['username'],
            password=md5(request.form['password']).hexdigest(),
            email=request.form['email'],)
    return redirect(url_for('hello'))
except IntegrityError:
    flash('That username is already taken')

user = get_object_or_404(User, username=username)
try:
    with database.atomic():
        Relationship.create(
            from_user=get_current_user(),
            to_user=user)
except IntegrityError:
    pass

class Relationship(BaseModel):
    from_user = ForeignKeyField(User, backref='relationships')
    to_user = ForeignKeyField(User, backref='related_to')

    class Meta:
        indexes = (
            (('from_user', 'to_user'), True),
        )

class Note(BaseModel):
    user = ForeignKeyField(User, backref='posts')
    title = CharField()
    text = TextField()

if __name__ == '__main__':
    app.run()
