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
from app import app, db, YMDish
from config import PER_PAGE

mod=Blueprint('ym_dishes',__name__)

@mod.route('/getTodayFoodList',methods=('GET', 'POST'))
def GetTodayFood():
    if request.method=='GET':
        return json.dumps({'message':'Please use method POST!'})
    if request.method=='POST':
        List=[]
        page=request.values.get('page')
        if page is None:
            i_page=1
        else:
            i_page=int(page)
        FoodList=YMDish.query.filter(YMDish.IsToday==True).paginate(i_page,PER_PAGE,False).items
        PageNum=YMDish.query.filter(YMDish.IsToday==True).paginate(i_page,PER_PAGE,False).pages
        if FoodList is None:
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
                         ,'Price':one.Price
                         ,'Like':one.Like
                         ,'Favorite':one.Favorite})
        return json.dumps({'CurrentPage':str(i_page)}
                          ,{'PageNum':str(PageNum)}
                          ,{'Dish_List',json.dumps(List)})