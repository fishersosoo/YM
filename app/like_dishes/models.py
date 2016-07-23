# -*- coding: utf-8 -*-
from app import db
from app.users import constants as USER
from flask_login import UserMixin
from collections import Counter

class LikeDish(db.Model):
    __tablename__='like_dish'
    UserName=db.Column(db.String(20),db.ForeignKey('_user.UserName'),primary_key=True,)
    DishID=db.Column(db.String(20),db.ForeignKey('ym_dish.DishID'),primary_key=True)
    def __init__(self,UserName,DishID):
        self.UserName=UserName
        self.DishID=DishID

    def save(self):
        db.session.add(self)
        db.session.commit()