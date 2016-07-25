# -*- coding: utf-8 -*-
from __future__ import absolute_import

import hashlib
import json
import types
from datetime import time
import time

from flask_bootstrap import Bootstrap
from flask import Blueprint, render_template, flash, redirect, session, url_for, request, g, make_response
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.favorite_dishes.models import FavoriteDish
from app.like_dishes.models import LikeDish
from app.users.forms import LoginForm
from app.users.forms import RegistrationForm
from app.users.models import User
from app.ym_dishes.models import YMDish

mod = Blueprint('favorite_dishes', __name__)


@mod.route('/getFavoriteDishes', methods=('GET', 'POST'))
def GetFavoriteDish():
    if request.method == 'GET':
        return json.dumps({'message': 'Please use method POST!'})
    if request.method == 'POST':
        token = request.values.get('token')
        if token is None:
            return json.dumps({'message': 'Need Token!'})
        user = User.verify_auth_token(token)
        if type(user) is types.StringType:
            return json.dumps({'message': user})
        like_diskes = db.session.query(YMDish).join(FavoriteDish).filter(FavoriteDish.UserName == user.UserName).all()
        List = []
        for one in like_diskes:
            List.append({'DishID': one.DishID
                            , 'DishType': one.DishType
                            , 'DishSmallImage': one.DishSmallImage
                            , 'DishLargeImage': one.DishLargeImage
                            , 'DishName': one.DishName
                            , 'Taste': one.Taste
                            , 'RawStuff': one.RawStuff
                            , 'Locations': one.Locations
                            , 'Description': one.Description
                            , 'Price': str(one.Price)
                            , 'Like': one.Like
                            , 'Favorite': one.Favorite})
        return json.dumps({'Dish_List': json.dumps(List)})


@mod.route('/favorite', methods=('GET', 'POST'))
def Favorite():
    if request.method == 'GET':
        return json.dumps({'message': 'Please use method POST!'})
    if request.method == 'POST':
        token = request.values.get('token')
        if token is None:
            return json.dumps({'message': 'Need Token!'})
        user = User.verify_auth_token(token)
        if type(user) is types.StringType:
            return json.dumps({'message': user})
        if request.values.get('DishID') is None:
            return json.dumps({'message': 'Need DishID!'})
        favorite_dish = FavoriteDish(DishID=request.values.get('DishID'), UserName=user.UserName)
        try:
            favorite_dish.save()
        except:
            return json.dumps({'message': 'Already Favorite!'})
        dish = YMDish.query.filter(request.values.get('DishID') == YMDish.DishID).first()
        dish.Favorite += 1
        dish.save()
        return json.dumps({'message': 'Favorite Success!'})


@mod.route('/dont_favorite', methods=('GET', 'POST'))
def DontFavorite():
    if request.method == 'GET':
        return json.dumps({'message': 'Please use method POST!'})
    if request.method == 'POST':
        token = request.values.get('token')
        if token is None:
            return json.dumps({'message': 'Need Token!'})
        user = User.verify_auth_token(token)
        if type(user) is types.StringType:
            return json.dumps({'message': user})
        if request.values.get('DishID') is None:
            return json.dumps({'message': 'Need DishID!'})
        like_dish = FavoriteDish.query.filter(FavoriteDish.DishID == request.values.get('DishID')
                                              , FavoriteDish.UserName == user.UserName).first()
        if like_dish is None:
            return json.dumps({'message': 'Not Favorite!'})
        db.session.delete(like_dish)
        db.session.commit()
        dish = YMDish.query.filter(YMDish.DishID == request.values.get('DishID')).first()
        dish.Favorite -= 1
        dish.save()
        return json.dumps({'message': 'Dont Favorite Success!'})
