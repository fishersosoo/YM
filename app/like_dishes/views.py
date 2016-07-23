# -*- coding: utf-8 -*-
from __future__ import absolute_import

import hashlib
import json
from datetime import time
import time
from sqlite3 import IntegrityError

from flask_bootstrap import Bootstrap
from flask import Blueprint, render_template, flash, redirect, session, url_for, request, g, make_response
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.users.forms import LoginForm
from app.users.forms import RegistrationForm


mod=Blueprint('like_dishes',__name__)

@mod.route('/index')
def index():
    return 1