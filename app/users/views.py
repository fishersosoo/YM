# -*- coding: utf-8 -*-
from __future__ import absolute_import


import json
import types
from datetime import time
import time
from sqlite3 import IntegrityError

from flask_bootstrap import Bootstrap
from flask import Blueprint, render_template, flash, redirect, session, url_for, request, g, make_response
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, users
<<<<<<< HEAD
from app.users.models import User

mod = Blueprint('users', __name__)


@mod.route('/Register', methods=('GET', 'POST'))
def Register():
    if request.method == 'GET':
        return json.dumps({'message': 'Please use method POST!'})
    if request.method == 'POST':
        user = User.query.filter(User.UserName == request.values.get('UserName')).first()
        if user != None:
            return json.dumps({'message': 'Username exist!'})
        user = User.query.filter(User.Email == request.values.get('Email')).first()
        if user != None:
            return json.dumps({'message': 'Email exist!'})
        user = User.query.filter(User.MobilePhoneNumber == request.values.get('MobilePhoneNumber')).first()
        if user != None:
            return json.dumps({'message': 'MobilePhoneNumber exist!'})
        user = User(UserName=request.values.get('UserName')
                    , Password=request.values.get('Password')
                    , Email=request.values.get('Email')
                    , EmailVerified=False
                    , MobilePhoneVerified=False
                    , NickName=request.values.get('NickName')
                    , Birthday=request.values.get('Birthday')
                    , Gender=request.values.get('Gender')
                    , Hometown=request.values.get('Hometown')
                    , MobilePhoneNumber=request.values.get('MobilePhoneNumber')
                    , Sentence=request.values.get('Sentence')
                    )
        try:
            user.save()
            return json.dumps({'message': 'Register Success!'})
        except:
            return json.dumps({'message': 'Register Failure!'})


@mod.route('/Login', methods=('GET', 'POST'))
def Login():
    if request.method == 'GET':
        return json.dumps({'message': 'Please use method POST!'})
    if request.method == 'POST':
        user = User.query.filter(User.UserName == request.values.get('UserName')).first()
        if user == None:
            return json.dumps({'message': 'UserName does not exist!'})
        if user.verify_password(request.values.get('Password')):
            return json.dumps({'message': 'Login Success!'
                                  , 'token': user.generate_auth_token()})
        else:
            return json.dumps({'message': 'Password is wrong!'})

=======
from app.users.models import Admin
>>>>>>> origin/manage

@mod.route('/getUserInfo', methods=('GET', 'POST'))
def GetUserInfo():
    if request.method=='GET':
        return json.dumps({'message': 'Please use method POST!'})
    if request.method == 'POST':
        token = request.values.get('token')
        if token is None:
            return json.dumps({'message': 'Need Token!'})
        user = User.verify_auth_token(token)
        if type(user) is types.StringType:
            return json.dumps({'message':user})
        info={  'UserName':user.UserName,
                'HeadImage':user.HeadImage,
                'Email':user.Email,
                'MobilePhoneNumber':user.MobilePhoneNumber,
                'MobilePhoneVerified':user.MobilePhoneVerified,
                'Hometown':user.Hometown,
                'Gender':user.Gender,
                'Birthday':str(user.Birthday),
                'Sentence':user.Sentence,
                'NickName':user.NickName
              }
        return json.dumps(info)

@mod.route('/editUserInfo', methods=('GET', 'POST'))
def EditUserInfo():
    if request.method=='GET':
        return json.dumps({'message': 'Please use method POST!'})
    if request.method == 'POST':
        token = request.values.get('token')
        if token is None:
            return json.dumps({'message': 'Need Token!'})
        user = User.verify_auth_token(token)
        if type(user) is types.StringType:
            return json.dumps({'message':user})
        if request.values.get('Email') !='':
            check = User.query.filter(User.Email == request.values.get('Email')).first()
            if check != None:
                return json.dumps({'message': 'Email exist!'})
        if request.values.get('MobilePhoneNumber') !='':
            check = User.query.filter(User.MobilePhoneNumber == request.values.get('MobilePhoneNumber')).first()
            if check != None:
                return json.dumps({'message':'MobilePhoneNumber exist!'})
        user.HeadImage=request.values.get('HeadImage')
        user.Email=request.values.get('Email')
        user.MobilePhoneNumber=request.values.get('MobilePhoneNumber')
        user.Hometown=request.values.get('Hometown')
        user.Gender=request.values.get('Gender')
        user.Birthday=request.values.get('Birthday')
        user.Sentence=request.values.get('Sentence')
        user.NickName=request.values.get('NickName')
        user.save()
        return json.dumps({'message':'Modify Succeed!'})

<<<<<<< HEAD
@mod.route('/changePassword', methods=('GET', 'POST'))
def ChangePassword():
    if request.method=='GET':
        return json.dumps({'message': 'Please use method POST!'})
    if request.method == 'POST':
        token = request.values.get('token')
        if token is None:
            return json.dumps({'message': 'Need Token!'})
        user = User.verify_auth_token(token)
        if type(user) is types.StringType:
            return json.dumps({'message':user})
        if user.change_password(request.values.get('old_password'),request.values.get('new_password')):
            return json.dumps({'message': 'Change Succeed!'})
        else:
            return json.dumps({'message': 'Password is wrong!'})
=======
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
>>>>>>> origin/manage
