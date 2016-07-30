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
from app import app, db, users
from app.users.models import Admin


mod=Blueprint('users',__name__)

@mod.route('/adminLogin',methods=['GET','POST'])
def adminLogin():
    if request.method=='GET':
    	return json.dumps({'message':'Please use method POST!'})
    if request.method=='POST':
    	admin=Admin.query.filter(Admin.AdminName == request.values.get('AdminName')).first()
    	if admin == None:
    		return json.dumps({'message':'AdminName does not exist!'})
    	if admin.verify_password(request.values.get('Password')):
    		return json.dumps({'message':'Login Success!','token':admin.generate_auth_token()})
    	else:
    		return json.dumps({'message':'Password is wrong!'})
