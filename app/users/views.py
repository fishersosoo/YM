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
from app import app, db, User

mod=Blueprint('users',__name__)

@mod.route('/Register',methods=('GET', 'POST'))
def Register():
    if request.method=='GET':
        return json.dumps({'message':'Please use method POST!'})
    if request.method=='POST':
        user=User.query.filter(User.UserName==request.values.get('UserName')).first()
        if user!=None:
            return json.dumps({'message':'Username exist!'})
        user=User.query.filter(User.Email==request.values.get('Email')).first()
        if user!=None:
            return json.dumps({'message':'Email exist!'})
        user=User.query.filter(User.MobilePhoneNumber==request.values.get('MobilePhoneNumber')).first()
        if user!=None:
            return json.dumps({'message':'MobilePhoneNumber exist!'})
        user=User(UserName=request.values.get('UserName')
                  ,Password=request.values.get('Password')
                  ,Email=request.values.get('Email')
                  ,NickName=request.values.get('NickName')
                  ,Birthday=request.values.get('Birthday')
                  ,Gender=request.values.get('Gender')
                  ,HomeTown=request.values.get('HomeTown')
                  ,MobilePhoneNumber=request.values.get('MobilePhoneNumber')
                  )
        try :
            user.save()
            return json.dumps({'message':'Register Success!'})
        except :
            return json.dumps({'message':'Register Failure!'})

@mod.route('/Login',methods=('GET', 'POST'))
def Login():
    if request.method=='GET':
        return json.dumps({'message':'Please use method POST!'})
    if request.method=='POST':
        user=User.query.filter(User.UserName==request.values.get('UserName')).first()
        if user==None:
            return json.dumps({'message':'UserName does not exist!'})
        if user.verify_password(request.values.get('Password')):
            return json.dumps({'message':'UserName does not exist!'}
                              ,{'token':user.generate_auth_token()})
        else:
            return json.dumps({'message':'Password is wrong!'})
