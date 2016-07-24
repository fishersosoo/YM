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
from app.like_dishes.models import LikeDish
from app.users.models import User
from app.ym_dishes.models import YMDish


mod=Blueprint('like_dishes',__name__)


@mod.route('/getLikeDishes',methods=('GET', 'POST'))
def GetLikeDish():
    if request.method=='GET':
        return json.dumps({'message':'Please use method POST!'})
    if request.method=='POST':
        token=request.values.get('token')
        if token is None:
            return json.dumps({'message':'Need Token!'})
        user=User.verify_auth_token(token)
        if type(user) is types.StringType:
            return json.dumps({'message':user})
        like_diskes=db.session.query(YMDish).join(LikeDish).filter(LikeDish.UserName==user.UserName).all()
        List=[]
        for one in like_diskes:
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
        return json.dumps({'Dish_List':json.dumps(List)})

@mod.route('/like',methods=('GET','POST'))
def Like():
    if request.method=='GET':
        return json.dumps({'message':'Please use method POST!'})
    if request.method=='POST':
        token=request.values.get('token')
        if token is None:
            return json.dumps({'message':'Need Token!'})
        user=User.verify_auth_token(token)
        if type(user) is types.StringType:
            return json.dumps({'message':user})
        if request.values.get('DishID') is None:
            return json.dumps({'message':'Need DishID!'})
        like_dish=LikeDish(DishID=request.values.get('DishID'),UserName=user.UserName)
        try:
            like_dish.save()
        except :
            return json.dumps({'message':'Already like!'})
        dish=YMDish.query.filter(YMDish.DishID==request.values.get('DishID')).first()
        dish.Like=dish.Like+1
        dish.save()
        return json.dumps({'message':'Like Success!'})


@mod.route('/dont_like',methods=('GET','POST'))
def DontLike():
    if request.method=='GET':
        return json.dumps({'message':'Please use method POST!'})
    if request.method=='POST':
        token=request.values.get('token')
        if token is None:
            return json.dumps({'message':'Need Token!'})
        user=User.verify_auth_token(token)
        if type(user) is types.StringType:
            return json.dumps({'message':user})
        if request.values.get('DishID') is None:
            return json.dumps({'message':'Need DishID!'})
        like_dish=LikeDish.query.filter(LikeDish.DishID==request.values.get('DishID')
                                        ,LikeDish.UserName==user.UserName).first()
        if like_dish is None:
            return json.dumps({'message':'Not Like!'})
        db.session.delete(like_dish)
        db.session.commit()
        dish=YMDish.query.filter(YMDish.DishID==request.values.get('DishID')).first()
        dish.Like=dish.Like-1
        dish.save()
        return json.dumps({'message':'Dont Like Success!'})
