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
from app.users.models import User
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
        comments=YMDishComment.query.filter(YMDishComment.DishID==request.values.get('DishID')).paginate(i_page,PER_PAGE,False).items
        PageNum=YMDishComment.query.filter(YMDishComment.DishID==request.values.get('DishID')).paginate(i_page,PER_PAGE,False).pages
        if len(comments) == 0:
            return json.dumps({'message':'Page is out of range!'})
        for one in comments:
            List.append({'Time':str(one.Time)
                        ,'Content':one.Content
                        ,'NickName':User.query.filter(User.UserName==one.UserName).first().NickName})
        return json.dumps({'CurrentPage':str(i_page)
                          ,'PageNum':str(PageNum)
                          ,'comment_list':json.dumps(List)})

@mod.route('/createComment',methods=('GET', 'POST'))
def CreateComment():
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
        if YMDish.query.filter(YMDish.DishID==request.values.get('DishID')).all() is None:
            return json.dumps({'message':'DishID is invalid!'})
        if request.values.get('Content') is None:
            return json.dumps({'message':'Need Content!'})

        else:
            ym_dish_comments=YMDishComment(UserName=user.UserName,DishID=request.values.get('DishID')
                                           ,Time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                                           ,Content=request.values.get('Content'))
            try:
                ym_dish_comments.save()
            except:
                return json.dumps({'message':'Comment Existed!'})
            return json.dumps({'message':'Add Comment Success!'})

