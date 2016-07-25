# -*- coding: utf-8 -*-
from __future__ import absolute_import
from flask_bootstrap import Bootstrap
from flask import Flask, g, render_template, send_from_directory, session, request
import os
import os.path

from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect



_basedir = os.path.abspath(os.path.dirname(__file__))
configPy = os.path.join(os.path.join(_basedir, os.path.pardir), 'config.py')

app = Flask(__name__)
Bootstrap(app)
app.config.from_pyfile(configPy)

flask_sqlalchemy_used = True
db = SQLAlchemy(app)

from app.users.views import mod as usersModule
from app.ym_dishes.views import mod as ym_dishesModule
from app.favorite_dishes.views import mod as favorite_dishesModule
from app.like_dishes.views import mod as like_dishesModule
from app.ym_dish_comments.views import mod as ym_dish_commentsModule


app.register_blueprint(usersModule,url_prefix='/users')
app.register_blueprint(favorite_dishesModule,url_prefix='/favorite_dishes')
app.register_blueprint(like_dishesModule,url_prefix='/like_dishes')
app.register_blueprint(ym_dish_commentsModule,url_prefix='/ym_dish_comments')
app.register_blueprint(ym_dishesModule,url_prefix='/ym_dishes')




auth = HTTPBasicAuth()



# *****************
# controllers
# *****************

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.route("/")
def index():
    return render_template('index.html')


