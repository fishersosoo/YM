# -*- coding: utf-8 -*-
from __future__ import absolute_import

import hashlib
import json
from datetime import time
import types
import time
from sqlite3 import IntegrityError

from flask_bootstrap import Bootstrap
from flask import Blueprint, render_template, flash, redirect, session, url_for, request, g, make_response
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db

from app.users.models import User,Admin
from app.ym_dish_comments.models import YMDishComment
from app.ym_dishes.models import YMDish
from config import PER_PAGE


mod=Blueprint('ym_dish_comments',__name__)

@mod.route('/getCommentList',methods=('GET', 'POST'))
def GetCommentList():
	if request.method=='GET':
		return json.dumps({'message':'Please use method POST!'})
	if request.method=='POST':
		List=[]
		page=request.values.get('page')
		if page is None:
			i_page=1
		else:
			i_page=int(page)

		if request.values.get('DishID') is None:
			return json.dumps({'message':'Need DishID!'})

		if YMDish.query.filter(YMDish.DishID==request.values.get('DishID')).first() is None:
			return json.dumps({'message':'DishID is invalid!'})

		comments=YMDishComment.query.filter(YMDishComment.DishID==request.values.get('DishID')).paginate(i_page,PER_PAGE,False).items
		PageNum=YMDishComment.query.filter(YMDishComment.DishID==request.values.get('DishID')).paginate(i_page,PER_PAGE,False).pages
		
		if len(comments) == 0 and i_page>1:
			return json.dumps({'message':'Page is out of range!'})

		for one in comments:
			List.append({'Time':str(one.Time)
						,'Content':one.Content
						,'NickName':User.query.filter(User.UserName==one.UserName).first().NickName})
		return json.dumps({'CurrentPage':str(i_page)
						,'PageNum':str(PageNum)
						,'Comment_List':json.dumps(List)})

@mod.route('/adminGetCommentList',methods=('GET', 'POST'))
def adminGetCommentList():
	if request.method=='GET':
		return json.dumps({'message':'Please use method POST!'})
	if request.method=='POST':
		List=[]
		page=request.values.get('Page')
		if page is None:
			i_page=1
		else:
			i_page=int(page)

		if request.values.get('DishID') is None:
			return json.dumps({'message':'Need DishID!'})

		if YMDish.query.filter(YMDish.DishID==request.values.get('DishID')).first() is None:
			return json.dumps({'message':'DishID is invalid!'})

		comments=YMDishComment.query.filter(YMDishComment.DishID==request.values.get('DishID')).paginate(i_page,PER_PAGE,False).items
		PageNum=YMDishComment.query.filter(YMDishComment.DishID==request.values.get('DishID')).paginate(i_page,PER_PAGE,False).pages
		
		if len(comments) == 0 and i_page>1:
			return json.dumps({'message':'Page is out of range!'})

		for one in comments:
			List.append({'Time':str(one.Time)
						,'Content':one.Content
						,'NickName':User.query.filter(User.UserName==one.UserName).first().NickName
						,'UserName':one.UserName})
		return json.dumps({'CurrentPage':str(i_page)
						,'PageNum':str(PageNum)
						,'Comment_List':json.dumps(List)})

@mod.route('/adminDeleteComment',methods=['GET','POST'])
def adminDeleteComment():
	if request.method == 'GET':
		return json.dumps({'message':'Please use method POST!'})
	if request.method == 'POST':
		# validate admin
		token = request.values.get('token')
		if token is None:
			return json.dumps({'message': 'Need Token!'})
		
		admin = Admin.verify_auth_token(token)
		if type(admin) is types.StringType:
			return json.dumps({'message':admin})
			
		if request.values.get('DishID') is None:
			return json.dumps({'message':'Need DishID!'})

		if YMDish.query.filter(YMDish.DishID==request.values.get('DishID')).first() is None:
			return json.dumps({'message':'DishID is invalid!'})
			
		if request.values.get('UserName') is None:
			return json.dumps({'message':'Need UserName!'})

		comment=YMDishComment.query.filter(YMDishComment.DishID==request.values.get('DishID'),\
			YMDishComment.UserName==request.values.get('UserName')).first()
		if comment is None:
			return json.dumps({'message':'Comment does not exist!'})

		db.session.delete(comment)
		db.session.commit()

		return json.dumps({'message':'Delete Succeed!'})