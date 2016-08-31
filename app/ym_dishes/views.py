# -*- coding: utf-8 -*-
from __future__ import absolute_import

import hashlib
import json
import types
from datetime import time
import time
from sqlite3 import IntegrityError

from flask_bootstrap import Bootstrap
from flask import Blueprint, render_template, flash, redirect, session, url_for, request, g, make_response
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from config import PER_PAGE
from app.users.models import Admin
from app.ym_dishes.models import YMDish



mod=Blueprint('ym_dishes',__name__)

def test(obj):
	print obj

@mod.route('/adminGetFoodList',methods=['GET','POST'])
def adminGetFoodList():
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
		
		# get foodlist
		List=[]
		page = request.values.get('Page')
		if page is None:
			i_page=1
		else:
			i_page=int(page)
		FoodList=YMDish.query.paginate(i_page,PER_PAGE,False).items
		PageNum=YMDish.query.paginate(i_page,PER_PAGE,False).pages
		if len(FoodList)==0 and i_page>1:
			return json.dumps({'message':'Page is out of range!'})
		for one in FoodList:
			List.append({'DishID':one.DishID
						,'DishType':one.DishType
						,'DishSmallImage':one.DishSmallImage
						,'DishLargeImage':one.DishLargeImage
						,'DishName':one.DishName
						,'Taste':one.Taste
						,'RawStuff':one.RawStuff
						,'Locations':one.Locations
						,'Description':one.Description
						,'Price':str(one.Price)
						,'Like':one.Like
						,'Favorite':one.Favorite
						,'IsToday':one.IsToday})

		return json.dumps({'CurrentPage':str(i_page)
						,'PageNum':str(PageNum)
						,'Dish_List':json.dumps(List)})


@mod.route('/adminModifyDish',methods=['GET','POST'])
def adminModifyDish():
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

		dish = YMDish.query.filter(YMDish.DishID==request.values.get('DishID')).first() 
		if dish is None:
			return json.dumps({'message':'DishID is invalid!'})
		
		dish.DishType= request.values.get('DishType')
		dish.DishSmallImage=request.values.get('DishSmallImage')
		dish.DishLargeImage=request.values.get('DishLargeImage')
		dish.DishName=request.values.get('DishName')
		dish.Taste=request.values.get('Taste')
		dish.RawStuff=request.values.get('RawStuff')
		dish.Locations=request.values.get('Locations')
		dish.Description=request.values.get('Description')
		dish.Price=request.values.get('Price')

		dish.save()

		return json.dumps({'message':'Modify Succeed!'})


@mod.route('/adminAddDish',methods=['GET','POST'])
def adminAddDish():
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
			
		dish = YMDish.query.filter(YMDish.DishID==request.values.get('DishID')).first() 
		if dish is not None:
			return json.dumps({'message':'DishID Existed!'})
			
		dish=YMDish(DishID=request.values.get('DishID')
			,DishType=request.values.get('DishType')
			,DishSmallImage=request.values.get('DishSmallImage')
			,DishLargeImage=request.values.get('DishLargeImage')
			,DishName=request.values.get('DishName')
			,Taste=request.values.get('Taste')
			,RawStuff=request.values.get('RawStuff')
			,Locations=request.values.get('Locations')
			,Description=request.values.get('Description')
			,Price=request.values.get('Price')
			,Like=0
			,Favorite=0
			,IsToday=False)

		dish.save()
		return json.dumps({'message':'Add Dish Succeed!'})


@mod.route('/adminDelDish',methods=['GET','POST'])
def adminDelDish():
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
	
		dish = YMDish.query.filter(YMDish.DishID==request.values.get('DishID')).first() 
		if dish is None:
			return json.dumps({'message':'DishID is invalid!'})

		db.session.delete(dish)
		db.session.commit()

		return json.dumps({'message':'Delete Dish Succeed!'})


@mod.route('/getTodayFoodList',methods=('GET', 'POST'))
def GetTodayDish():
	if request.method=='GET':
		return json.dumps({'message':'Please use method POST!'})
	if request.method=='POST':
		List=[]
		page=request.values.get('Page')
		if page is None:
			i_page=1
		else:
			i_page=int(page)

		FoodList=YMDish.query.filter(YMDish.IsToday==True).paginate(i_page,PER_PAGE,False).items
		PageNum=YMDish.query.filter(YMDish.IsToday==True).paginate(i_page,PER_PAGE,False).pages
		if len(FoodList) == 0 and i_page>1:
			return json.dumps({'message':'Page is out of range!'})
		for one in FoodList:
			List.append({'DishID':one.DishID
						 ,'DishType':one.DishType
						 ,'DishSmallImage':one.DishSmallImage
						 ,'DishLargeImage':one.DishLargeImage
						 ,'DishName':one.DishName
						 ,'Taste':one.Taste
						 ,'RawStuff':one.RawStuff
						 ,'Locations':one.Locations
						 ,'Description':one.Description
						 ,'Price':str(one.Price)
						 ,'Like':one.Like
						 ,'Favorite':one.Favorite})
		return json.dumps({'CurrentPage':str(i_page)
						  ,'PageNum':str(PageNum)
						  ,'Dish_List':json.dumps(List)})


@mod.route('/adminOperateTodayDish/<op>',methods=['GET','POST'])
def adminOperateTodayDish(op):
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
	
		dish = YMDish.query.filter(YMDish.DishID==request.values.get('DishID')).first() 
		if dish is None:
			return json.dumps({'message':'DishID is invalid!'})

		if op == 'del':
			dish.IsToday=False
		if op == 'add':
			dish.IsToday=True

		dish.save()
		return json.dumps({'message':'Modify Succeed!'})