# -*- coding: utf-8 -*-
from __future__ import absolute_import
from flask_bootstrap import Bootstrap
from flask import Flask, g, render_template, send_from_directory, session, request
import os
import os.path

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
from app.users.models import User
from app.ym_dishes.models import YMDish
from app.favorite_dishes.models import FavoriteDish
from app.like_dishes.models import LikeDish
from app.ym_dish_comments.models import YMDishComment
db.create_all()


# *****************
# controllers
# *****************

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    print request.values
    return render_template('404.html'), 404


@app.route("/")
def index():
    return render_template('index.html')


